from PySide6 import QtGui, QtWidgets
from mapclientplugins.pointwiserigidregistrationstep.ui_configuredialog import Ui_Dialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, reg_methods, parent=None):
        """
        Constructor
        """
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._regMethods = reg_methods
        self._setup_dialog()
        self._make_connections()

    def _setup_dialog(self):
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

    def _make_connections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)

        self._ui.txLineEdit.textChanged.connect(self._fields_updated)
        self._ui.tyLineEdit.textChanged.connect(self._fields_updated)
        self._ui.tzLineEdit.textChanged.connect(self._fields_updated)

        self._ui.rxLineEdit.textChanged.connect(self._fields_updated)
        self._ui.ryLineEdit.textChanged.connect(self._fields_updated)
        self._ui.rzLineEdit.textChanged.connect(self._fields_updated)

        self._ui.sLineEdit.textChanged.connect(self._fields_updated)

    def _fields_updated(self):
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
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.StandardButton.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration', 'This configuration is invalid.  Unpredictable behaviour '
                                                   'may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                                                   QtWidgets.QMessageBox.StandardButton.No)

        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        self._ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(valid)
        return valid

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.lineEdit0.text()
        config = {
            'identifier': self._ui.lineEdit0.text(),
            'UI Mode': self._ui.UICheckBox.isChecked(),
            'Registration Method': self._ui.regMethodsComboBox.currentText(),
            'Min Relative Error': self._ui.xtolLineEdit.text(),
            'Points to Sample': self._ui.sampleLineEdit.text(),
            'Init Trans': [float(self._ui.txLineEdit.text()),
                           float(self._ui.tyLineEdit.text()),
                           float(self._ui.tzLineEdit.text())],
            'Init Rot': [float(self._ui.rxLineEdit.text()),
                         float(self._ui.ryLineEdit.text()),
                         float(self._ui.rzLineEdit.text())],
            'Init Scale': float(self._ui.sLineEdit.text())
        }
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])
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
