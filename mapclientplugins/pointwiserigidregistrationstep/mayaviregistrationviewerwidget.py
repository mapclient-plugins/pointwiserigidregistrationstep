"""
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland

This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
"""
import os

from PySide6.QtWidgets import QDialog, QAbstractItemView, QTableWidgetItem
from PySide6.QtGui import QDoubleValidator, QIntValidator, Qt
from PySide6.QtCore import Qt
from PySide6.QtCore import QThread, Signal

from mapclientplugins.pointwiserigidregistrationstep.ui_mayaviregistrationviewerwidget import Ui_Dialog
from traits.api import on_trait_change

import numpy as np
from gias3.common import math
from gias3.mapclientpluginutilities.viewers import MayaviViewerObjectsContainer, colours
from gias3.mapclientpluginutilities.viewers.mayaviviewerdatapoints import MayaviViewerDataPoints

os.environ['ETS_TOOLKIT'] = 'qt'


class _ExecThread(QThread):
    update = Signal(tuple)

    def __init__(self, func):
        QThread.__init__(self)
        self.func = func

    def run(self):
        output = self.func()
        self.update.emit(output)


class MayaviRegistrationViewerWidget(QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """
    defaultColor = colours['bone']
    objectTableHeaderColumns = {'visible': 0, 'type': 1}
    backgroundColour = (0.0, 0.0, 0.0)
    _sourceRenderArgs = {'mode': 'point', 'scale_factor': 0.1, 'color': (0, 1, 0)}
    _targetRenderArgs = {'mode': 'point', 'scale_factor': 0.1, 'color': (1, 0, 0)}
    _registeredRenderArgs = {'mode': 'point', 'scale_factor': 0.1, 'color': (1, 1, 0)}

    def __init__(self, source_data, target_data, config, register_func,
                 reg_methods, manual_transform_func, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._scene = self._ui.MayaviScene.visualisation.scene
        self._scene.background = self.backgroundColour

        self.selectedObjectName = None
        self._sourceData = source_data
        self._targetData = target_data
        self._sourceDataAligned = None
        self._registerFunc = register_func
        self._regMethods = reg_methods
        self._manualTransform = manual_transform_func
        self._config = config
        self._enableManualUpdate = True

        self._worker = _ExecThread(self._registerFunc)
        self._worker.update.connect(self._reg_update)

        # print 'init...', self._config

        # create self._objects
        self._objects = MayaviViewerObjectsContainer()
        self._objects.addObject('source',
                                MayaviViewerDataPoints('source', self._sourceData, render_args=self._sourceRenderArgs))
        self._objects.addObject('target',
                                MayaviViewerDataPoints('target', self._targetData, render_args=self._targetRenderArgs))
        self._objects.addObject('registered', MayaviViewerDataPoints('registered', self._sourceData,
                                                                     render_args=self._registeredRenderArgs))

        self._setup_gui()
        self._make_connections()
        self._initialise_object_table()
        self._initialise_settings()
        self._refresh()

        # self.test_plot()
        # self.draw_objects()
        print('finished init...', self._config)

    def _setup_gui(self):
        self._ui.samplesLineEdit.setValidator(QIntValidator())
        self._ui.xtolLineEdit.setValidator(QDoubleValidator())

    def _make_connections(self):
        self._ui.tableWidget.itemClicked.connect(self._table_item_clicked)
        self._ui.tableWidget.itemChanged.connect(self._visible_box_changed)
        self._ui.screenshotSaveButton.clicked.connect(self._save_screen_shot)

        # clicking register spawns a thread, need to lock parts of ui
        self._ui.registerButton.clicked.connect(self._worker.start)
        self._ui.registerButton.clicked.connect(self._reg_lock_ui)

        self._ui.resetButton.clicked.connect(self._reset)
        self._ui.abortButton.clicked.connect(self._abort)
        self._ui.acceptButton.clicked.connect(self._accept)

        self._ui.regMethodsComboBox.activated.connect(self._update_config_reg_method)
        self._ui.xtolLineEdit.textChanged.connect(self._update_config_xtol)
        self._ui.samplesLineEdit.textChanged.connect(self._update_config_samples)

        self._ui.doubleSpinBox_tx.valueChanged.connect(self._update_init_trans)
        self._ui.doubleSpinBox_ty.valueChanged.connect(self._update_init_trans)
        self._ui.doubleSpinBox_tz.valueChanged.connect(self._update_init_trans)

        self._ui.doubleSpinBox_rotx.valueChanged.connect(self._update_init_rot)
        self._ui.doubleSpinBox_roty.valueChanged.connect(self._update_init_rot)
        self._ui.doubleSpinBox_rotz.valueChanged.connect(self._update_init_rot)

        self._ui.doubleSpinBox_scale.valueChanged.connect(self._update_init_scale)

    def _initialise_settings(self):
        self._ui.xtolLineEdit.setText(self._config['Min Relative Error'])
        self._ui.samplesLineEdit.setText(self._config['Points to Sample'])

        # print 'initialising settings...', self._config

        for m in self._regMethods:
            self._ui.regMethodsComboBox.addItem(m)

        self._ui.regMethodsComboBox.setCurrentIndex(self._regMethods.index(self._config['Registration Method']))

        initTrans = self._config['Init Trans']
        # if isinstance(initTrans, (str, unicode)):
        #     initTrans = eval(initTrans)

        self._ui.doubleSpinBox_tx.setValue(float(initTrans[0]))
        self._ui.doubleSpinBox_ty.setValue(float(initTrans[1]))
        self._ui.doubleSpinBox_tz.setValue(float(initTrans[2]))

        initRot = self._config['Init Rot']
        # if isinstance(initRot, (str, unicode)):
        #     initRot = eval(initRot)
        self._ui.doubleSpinBox_rotx.setValue(float(initRot[0]))
        self._ui.doubleSpinBox_roty.setValue(float(initRot[1]))
        self._ui.doubleSpinBox_rotz.setValue(float(initRot[2]))

        self._ui.doubleSpinBox_scale.setValue(self._config['Init Scale'])
        # self._ui.doubleSpinBox_scale.setValue(float(self._config['Init Scale']))

    def _initialise_object_table(self):

        self._ui.tableWidget.setRowCount(self._objects.getNumberOfObjects())
        self._ui.tableWidget.verticalHeader().setVisible(False)
        self._ui.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self._ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self._ui.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self._add_object_to_table(0, 'source', self._objects.getObject('source'))
        self._add_object_to_table(1, 'target', self._objects.getObject('target'))
        self._add_object_to_table(2, 'registered', self._objects.getObject('registered'), checked=False)

        self._ui.tableWidget.resizeColumnToContents(self.objectTableHeaderColumns['visible'])
        self._ui.tableWidget.resizeColumnToContents(self.objectTableHeaderColumns['type'])

    def _add_object_to_table(self, row, name, obj, checked=True):
        typeName = obj.typeName
        tableItem = QTableWidgetItem(name)
        if checked:
            tableItem.setCheckState(Qt.Checked)
        else:
            tableItem.setCheckState(Qt.Unchecked)

        self._ui.tableWidget.setItem(row, self.objectTableHeaderColumns['visible'], tableItem)
        self._ui.tableWidget.setItem(row, self.objectTableHeaderColumns['type'], QTableWidgetItem(typeName))

    def _table_item_clicked(self):
        selectedRow = self._ui.tableWidget.currentRow()
        self.selectedObjectName = self._ui.tableWidget.item(selectedRow,
                                                            self.objectTableHeaderColumns['visible']).text()
        self._populateScalarsDropDown(self.selectedObjectName)

    def _visible_box_changed(self, table_item):
        # get name of object selected
        # name = self._get_selected_object_name()

        # checked changed item is actually the checkbox
        if table_item.column() == self.objectTableHeaderColumns['visible']:
            # get visible status
            name = table_item.text()
            visible = table_item.checkState() == Qt.CheckState.Checked

            print('visibleboxchanged name', name)
            print('visibleboxchanged visible', visible)

            # toggle visibility
            obj = self._objects.getObject(name)
            print(obj.name)
            if obj.sceneObject:
                print('changing existing visibility')
                obj.setVisibility(visible)
            else:
                print('drawing new')
                obj.draw(self._scene)

    def _get_selected_object_name(self):
        return self.selectedObjectName

    def draw_objects(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).draw(self._scene)

    def _update_config_reg_method(self):
        self._config['Registration Method'] = self._ui.regMethodsComboBox.currentText()

    def _update_config_xtol(self):
        self._config['Min Relative Error'] = self._ui.xtolLineEdit.text()

    def _update_config_samples(self):
        self._config['Points to Sample'] = self._ui.samplesLineEdit.text()

    def _update_init_trans(self):
        tx = self._ui.doubleSpinBox_tx.value()
        ty = self._ui.doubleSpinBox_ty.value()
        tz = self._ui.doubleSpinBox_tz.value()

        self._config['Init Trans'] = [tx, ty, tz]
        self._manual_update()

    def _update_init_rot(self):
        rx = self._ui.doubleSpinBox_rotx.value()
        ry = self._ui.doubleSpinBox_roty.value()
        rz = self._ui.doubleSpinBox_rotz.value()

        self._config['Init Rot'] = [rx, ry, rz]
        self._manual_update()

    def _update_init_scale(self):
        s = self._ui.doubleSpinBox_scale.value()
        self._config['Init Scale'] = s
        self._manual_update()

    def _manual_update(self):
        """Called when init translation, rotation and scale spinboxes
        are changed
        """
        if self._enableManualUpdate:
            transform, self._registeredData = self._manualTransform()
            regObj = self._objects.getObject('registered')
            regObj.updateGeometry(self._registeredData, self._scene)
            regTableItem = self._ui.tableWidget.item(2, self.objectTableHeaderColumns['visible'])
            regTableItem.setCheckState(Qt.Checked)

    def _reg_update(self, reg_output):
        # update registered datacloud
        transform, regData, rmse = reg_output
        self._registeredData = regData
        regObj = self._objects.getObject('registered')
        regObj.updateGeometry(self._registeredData, self._scene)
        regTableItem = self._ui.tableWidget.item(2, self.objectTableHeaderColumns['visible'])
        regTableItem.setCheckState(Qt.Checked)

        # update transformation spinboxes
        if self._config['Registration Method'] != 'Correspondent Affine':
            self._update_transform_boxes(transform.T)

        # update error fields
        self._ui.RMSELineEdit.setText(str(rmse))

        # unlock reg ui
        self._reg_unlock_ui()

    def _update_transform_boxes(self, transformation):
        # self._enableManualUpdate = False
        t = transformation[:3]
        r = transformation[3:6]
        self._ui.doubleSpinBox_tx.setValue(t[0])
        self._ui.doubleSpinBox_ty.setValue(t[1])
        self._ui.doubleSpinBox_tz.setValue(t[2])
        self._ui.doubleSpinBox_rotx.setValue(np.rad2deg(math.trimAngle(r[0])))
        self._ui.doubleSpinBox_roty.setValue(np.rad2deg(math.trimAngle(r[1])))
        self._ui.doubleSpinBox_rotz.setValue(np.rad2deg(math.trimAngle(r[2])))
        if len(transformation) > 6:
            s = transformation[6]
            self._ui.doubleSpinBox_scale.setValue(s)

        # self._enableManualUpdate = True

    def _reg_lock_ui(self):
        self._ui.regMethodsComboBox.setEnabled(False)
        self._ui.xtolLineEdit.setEnabled(False)
        self._ui.samplesLineEdit.setEnabled(False)
        self._ui.doubleSpinBox_tx.setEnabled(False)
        self._ui.doubleSpinBox_ty.setEnabled(False)
        self._ui.doubleSpinBox_tz.setEnabled(False)
        self._ui.doubleSpinBox_rotx.setEnabled(False)
        self._ui.doubleSpinBox_roty.setEnabled(False)
        self._ui.doubleSpinBox_rotz.setEnabled(False)
        self._ui.doubleSpinBox_scale.setEnabled(False)
        self._ui.registerButton.setEnabled(False)
        self._ui.resetButton.setEnabled(False)
        self._ui.acceptButton.setEnabled(False)
        self._ui.abortButton.setEnabled(False)

    def _reg_unlock_ui(self):
        self._ui.regMethodsComboBox.setEnabled(True)
        self._ui.xtolLineEdit.setEnabled(True)
        self._ui.samplesLineEdit.setEnabled(True)
        self._ui.doubleSpinBox_tx.setEnabled(True)
        self._ui.doubleSpinBox_ty.setEnabled(True)
        self._ui.doubleSpinBox_tz.setEnabled(True)
        self._ui.doubleSpinBox_rotx.setEnabled(True)
        self._ui.doubleSpinBox_roty.setEnabled(True)
        self._ui.doubleSpinBox_rotz.setEnabled(True)
        self._ui.doubleSpinBox_scale.setEnabled(True)
        self._ui.registerButton.setEnabled(True)
        self._ui.resetButton.setEnabled(True)
        self._ui.acceptButton.setEnabled(True)
        self._ui.abortButton.setEnabled(True)

    def _reset(self):
        # delete viewer table row
        # self._ui.tableWidget.removeRow(2)
        # reset registered datacloud
        regObj = self._objects.getObject('registered')
        regObj.updateGeometry(self._sourceData, self._scene)
        regTableItem = self._ui.tableWidget.item(2, self.objectTableHeaderColumns['visible'])
        regTableItem.setCheckState(Qt.Unchecked)

        # clear spinboxes
        self._update_transform_boxes([0, 0, 0, 0, 0, 0, 1])

        # clear error fields
        self._ui.RMSELineEdit.clear()

    def _accept(self):
        self._close()

    def _abort(self):
        self._reset()
        self._close()

    def _close(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).remove()

        self._objects._objects = {}
        # self._objects == None

        # for r in xrange(self._ui.tableWidget.rowCount()):
        #     self._ui.tableWidget.removeRow(r)

    def _refresh(self):
        for r in range(self._ui.tableWidget.rowCount()):
            tableItem = self._ui.tableWidget.item(r, self.objectTableHeaderColumns['visible'])
            name = tableItem.text()
            visible = tableItem.checkState() == Qt.CheckState.Checked
            obj = self._objects.getObject(name)
            print(obj.name)
            if obj.sceneObject:
                print('changing existing visibility')
                obj.setVisibility(visible)
            else:
                print('drawing new')
                obj.draw(self._scene)

    def _save_screen_shot(self):
        filename = self._ui.screenshotFilenameLineEdit.text()
        width = int(self._ui.screenshotPixelXLineEdit.text())
        height = int(self._ui.screenshotPixelYLineEdit.text())
        self._scene.mlab.savefig(filename, size=(width, height))

    # ================================================================#
    @on_trait_change('scene.activated')
    def test_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.
        print('trait_changed')

        # We can do normal mlab calls on the embedded scene.
        self._scene.mlab.test_points3d()

    # def _saveImage_fired( self ):
    #     self.scene.mlab.savefig( str(self.saveImageFilename), size=( int(self.saveImageWidth), int(self.saveImageLength) ) )
