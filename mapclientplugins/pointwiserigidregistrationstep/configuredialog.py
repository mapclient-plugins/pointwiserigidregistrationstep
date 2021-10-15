from PySide2 import QtGui, QtWidgets
from mapclientplugins.pointwiserigidregistrationstep.ui_configuredialog import Ui_Dialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, regMethods, parent=None):
        '''
        Constructor
        '''
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._regMethods = regMethods
        self._setupDialog()
        self._makeConnections()

    def _setupDialog(self):
        for m in self._regMethods:
            self._ui.regMethodsComboBox.addItem(m)

        self._ui.sampleLineEdit.setValidator(QtGui.QIntValidator())
        self._ui.xtolLineEdit.setValidator(QtGui.QDoubleValidator())
        self._ui.txLineEdit.setValidator(QtGui.QDoubleValidator())
        self._ui.tyLineEdit.setValidator(QtGui.QDoubleValidator())
        self._ui.tzLineEdit.setValidator(QtGui.QDoubleValidator())
        self._ui.rxLineEdit.setValidator(QtGui.QDoubleValidator())
        self._ui.ryLineEdit.setValidator(QtGui.QDoubleValidator())
        self._ui.rzLineEdit.setValidator(QtGui.QDoubleValidator())
        self._ui.sLineEdit.setValidator(QtGui.QDoubleValidator())

    def _makeConnections(self):
        self._ui.txLineEdit.textChanged.connect(self._fieldsUpdated)
        self._ui.tyLineEdit.textChanged.connect(self._fieldsUpdated)
        self._ui.tzLineEdit.textChanged.connect(self._fieldsUpdated)

        self._ui.rxLineEdit.textChanged.connect(self._fieldsUpdated)
        self._ui.ryLineEdit.textChanged.connect(self._fieldsUpdated)
        self._ui.rzLineEdit.textChanged.connect(self._fieldsUpdated)

        self._ui.sLineEdit.textChanged.connect(self._fieldsUpdated)

    def _fieldsUpdated(self):
        if self._ui.txLineEdit.text() == '':
            self._ui.txLineEdit.setText('0')
        if self._ui.tyLineEdit.text() == '':
            self._ui.tyLineEdit.setText('0')
        if self._ui.tzLineEdit.text() == '':
            self._ui.tzLineEdit.setText('0')
        if self._ui.rxLineEdit.text() == '':
            self._ui.rxLineEdit.setText('0')
        if self._ui.ryLineEdit.text() == '':
            self._ui.ryLineEdit.setText('0')
        if self._ui.rzLineEdit.text() == '':
            self._ui.rzLineEdit.setText('0')
        if self._ui.sLineEdit.text() == '':
            self._ui.sLineEdit.setText('1.0')

    def accept(self):
        '''
        Override the accept method so that we can confirm saving an
        invalid configuration.
        '''
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                                                   'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        '''
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the 
        overall validity of the configuration.
        '''
        # It's not currently possible for the configuration to be invalid, we may want to update this.
        return True

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.
        '''
        config = {}
        config['UI Mode'] = self._ui.UICheckBox.isChecked()
        config['Registration Method'] = self._ui.regMethodsComboBox.currentText()
        config['Min Relative Error'] = self._ui.xtolLineEdit.text()
        config['Points to Sample'] = self._ui.sampleLineEdit.text()
        config['Init Trans'] = [float(self._ui.txLineEdit.text()),
                                float(self._ui.tyLineEdit.text()),
                                float(self._ui.tzLineEdit.text())]
        config['Init Rot'] = [float(self._ui.rxLineEdit.text()),
                              float(self._ui.ryLineEdit.text()),
                              float(self._ui.rzLineEdit.text())]
        config['Init Scale'] = float(self._ui.sLineEdit.text())
        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.
        '''
        self._ui.UICheckBox.setChecked(bool(config['UI Mode']))
        self._ui.regMethodsComboBox.setCurrentIndex(self._regMethods.index(config['Registration Method']))
        self._ui.xtolLineEdit.setText(config['Min Relative Error'])
        self._ui.sampleLineEdit.setText(config['Points to Sample'])
        initTrans = config['Init Trans']
        self._ui.txLineEdit.setText(str(initTrans[0]))
        self._ui.tyLineEdit.setText(str(initTrans[1]))
        self._ui.tzLineEdit.setText(str(initTrans[2]))
        initRot = config['Init Rot']
        self._ui.rxLineEdit.setText(str(initRot[0]))
        self._ui.ryLineEdit.setText(str(initRot[1]))
        self._ui.rzLineEdit.setText(str(initRot[2]))
        self._ui.sLineEdit.setText(str(config['Init Scale']))
