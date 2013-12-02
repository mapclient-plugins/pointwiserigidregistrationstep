'''
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
'''
import os
os.environ['ETS_TOOLKIT'] = 'qt4'

from PySide.QtGui import QDialog, QFileDialog, QDialogButtonBox, QAbstractItemView, QTableWidgetItem
from PySide.QtCore import Qt

from pointwiserigidregistrationstep.ui_mayaviregistrationviewerwidget import Ui_Dialog
from traits.api import HasTraits, Instance, on_trait_change, \
    Int, Dict

from mappluginutils.mayaviviewer import MayaviViewerObjectsContainer, MayaviViewerDataPoints, colours

class MayaviRegistrationViewerWidget(QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''
    defaultColor = colours['bone']
    objectTableHeaderColumns = {'visible':0, 'type':1}
    backgroundColour = (0.0,0.0,0.0)
    _sourceRenderArgs = {'mode':'point', 'scale_factor':0.1, 'color':(0,1,0)}
    _targetRenderArgs = {'mode':'point', 'scale_factor':0.1, 'color':(1,0,0)}
    _registeredRenderArgs = {'mode':'point', 'scale_factor':0.1, 'color':(1,1,0)}

    def __init__(self, sourceData, targetData, config, registerFunc, regMethods, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._scene = self._ui.MayaviScene.visualisation.scene
        self._scene.background = self.backgroundColour

        self.selectedObjectName = None
        self._sourceData = sourceData
        self._targetData = targetData
        self._sourceDataAligned = None
        self._registerFunc = registerFunc
        self._regMethods = regMethods
        self._config = config

        # create self._objects
        self._objects = MayaviViewerObjectsContainer()
        self._objects.addObject('source', MayaviViewerDataPoints('source', self._sourceData, renderArgs=self._sourceRenderArgs))
        self._objects.addObject('target', MayaviViewerDataPoints('target', self._targetData, renderArgs=self._targetRenderArgs))

        self._makeConnections()
        self._initialiseObjectTable()
        self._initialiseSettings()
        self._refresh()

        # self.testPlot()
        # self.drawObjects()

    def _makeConnections(self):
        self._ui.tableWidget.itemClicked.connect(self._tableItemClicked)
        self._ui.tableWidget.itemChanged.connect(self._visibleBoxChanged)
        self._ui.screenshotSaveButton.clicked.connect(self._saveScreenShot)
        self._ui.registerButton.clicked.connect(self._register)
        self._ui.resetButton.clicked.connect(self._reset)
        self._ui.abortButton.clicked.connect(self._abort)
        self._ui.acceptButton.clicked.connect(self._accept)

        self._ui.regMethodsComboBox.activated.connect(self._updateConfig)
        self._ui.xtolLineEdit.textChanged.connect(self._updateConfig)
        self._ui.samplesLineEdit.textChanged.connect(self._updateConfig)

    def _initialiseSettings(self):
        for m in self._regMethods:
            self._ui.regMethodsComboBox.addItem(m)

        self._ui.xtolLineEdit.setText(self._config['Min Relative Error'])
        self._ui.samplesLineEdit.setText(self._config['Points to Sample'])

    def _initialiseObjectTable(self):

        self._ui.tableWidget.setRowCount(self._objects.getNumberOfObjects())
        self._ui.tableWidget.verticalHeader().setVisible(False)
        self._ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        
        self._addObjectToTable(0, 'source', self._objects.getObject('source'))
        self._addObjectToTable(1, 'target', self._objects.getObject('target'))

        self._ui.tableWidget.resizeColumnToContents(self.objectTableHeaderColumns['visible'])
        self._ui.tableWidget.resizeColumnToContents(self.objectTableHeaderColumns['type'])

    def _addObjectToTable(self, row, name, obj):
        typeName = obj.typeName
        print typeName
        print name
        tableItem = QTableWidgetItem(name)
        tableItem.setCheckState(Qt.Checked)
        self._ui.tableWidget.setItem(row, self.objectTableHeaderColumns['visible'], tableItem)
        self._ui.tableWidget.setItem(row, self.objectTableHeaderColumns['type'], QTableWidgetItem(typeName))

    def _tableItemClicked(self):
        selectedRow = self._ui.tableWidget.currentRow()
        self.selectedObjectName = self._ui.tableWidget.item(selectedRow, self.objectTableHeaderColumns['visible']).text()
        self._populateScalarsDropDown(self.selectedObjectName)
        print selectedRow
        print self.selectedObjectName

    def _visibleBoxChanged(self, tableItem):
        # get name of object selected
        # name = self._getSelectedObjectName()

        # checked changed item is actually the checkbox
        if tableItem.column()==self.objectTableHeaderColumns['visible']:
            # get visible status
            name = tableItem.text()
            visible = tableItem.checkState().name=='Checked'

            print 'visibleboxchanged name', name
            print 'visibleboxchanged visible', visible

            # toggle visibility
            obj = self._objects.getObject(name)
            print obj.name
            if obj.sceneObject:
                print 'changing existing visibility'
                obj.setVisibility(visible)
            else:
                print 'drawing new'
                obj.draw(self._scene)

    def _getSelectedObjectName(self):
        return self.selectedObjectName

    def _getSelectedScalarName(self):
        return 'none'

    def drawObjects(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).draw(self._scene)

    def _updateConfig(self):
        self._config['Registration Method'] = self._ui.regMethodsCombox.currentText()
        self._config['Min Relative Error'] = self._ui.xtolLineEdit.text()
        self._config['Points to Sample'] = self._ui.samplesLineEdit.text()

    def _register(self):
        transform, self._registeredData, RMSE = self._registerFunc()
        registeredObj = MayaviViewerDataPoints('registered', self._registeredData, renderArgs=self._registeredRenderArgs)
        self._objects.addObject('registered', registeredObj)
        self._addObjectToTable(2, 'registered', registeredObj)
        print 'added registered data points'
        self._ui.tableWidget.resizeColumnToContents(self.objectTableHeaderColumns['visible'])
        self._ui.tableWidget.resizeColumnToContents(self.objectTableHeaderColumns['type'])

    def _reset(self):
        # delete viewer table row
        self._ui.tableWidget.removeRow(2)
        # delete scene object
        self._objects.getObject('registered').remove()

    def _accept(self):
        self._close()

    def _abort(self):
        self._close()

    def _close(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).remove()

        self._objects._objects = {}
        self._objects == None

        # for r in xrange(self._ui.tableWidget.rowCount()):
        #     self._ui.tableWidget.removeRow(r)

    def _refresh(self):
        for r in xrange(self._ui.tableWidget.rowCount()):
            tableItem = self._ui.tableWidget.item(r, self.objectTableHeaderColumns['visible'])
            name = tableItem.text()
            visible = tableItem.checkState().name=='Checked'
            obj = self._objects.getObject(name)
            print obj.name
            if obj.sceneObject:
                print 'changing existing visibility'
                obj.setVisibility(visible)
            else:
                print 'drawing new'
                obj.draw(self._scene)

    def _saveScreenShot(self):
        filename = self._ui.screenshotFilenameLineEdit.text()
        width = int(self._ui.screenshotPixelXLineEdit.text())
        height = int(self._ui.screenshotPixelYLineEdit.text())
        self._scene.mlab.savefig( filename, size=( width, height ) )

    #================================================================#
    @on_trait_change('scene.activated')
    def testPlot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.
        print 'trait_changed'

        # We can do normal mlab calls on the embedded scene.
        self._scene.mlab.test_points3d()


    # def _saveImage_fired( self ):
    #     self.scene.mlab.savefig( str(self.saveImageFilename), size=( int(self.saveImageWidth), int(self.saveImageLength) ) )
        