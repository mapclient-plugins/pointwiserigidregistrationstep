
'''
MAP Client Plugin Step
'''
import os

from PySide import QtGui
from PySide import QtCore

from mountpoints.workflowstep import WorkflowStepMountPoint
from pointwiserigidregistrationstep.configuredialog import ConfigureDialog

from gias.common import alignment_fitting as AF
from pointwiserigidregistrationstep.mayaviregistrationviewerwidget import MayaviRegistrationViewerWidget

regMethods = {
              'Correspondent Rigid': AF.fitRigid,
              'Correspondent Rigid+Scale': AF.fitRigidScale,
              'Correspondent Affine': AF.fitAffine,
              'ICP Rigid Source-Target': AF.fitDataRigidEPDP,
              'ICP Rigid Target-Source': AF.fitDataRigidDPEP,
              'ICP Rigid+Scale Source-Target': AF.fitDataRigidScaleEPDP,
              'ICP Rigid+Scale Target-Source': AF.fitDataRigidScaleDPEP,
             }

class PointWiseRigidRegistrationStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(PointWiseRigidRegistrationStep, self).__init__('Point-wise Rigid Registration', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Registration'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#pointcoordinates'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#pointcoordinates'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#pointcoordinates'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#rigidtransformvector'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'float'))
        self._config = {}
        self._config['identifier'] = ''
        self._config['UI Mode'] = 'True'
        self._config['Registration Method'] = 'Correspondent Affine'
        self._config['Min Relative Error'] = '1e-3'
        self._config['Points to Sample'] = '1000'

        self.sourceData = None
        self.targetData = None
        self.sourceDataAligned = None
        self.transform = None
        self.RMSE = None

        self._widget = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        print 'fong', self._config['Points to Sample']
        # Put your execute step code here before calling the '_doneExecution' method.
        if self._config['UI Mode']=='True':
            self._widget = MayaviRegistrationViewerWidget(self.sourceData, self.targetData, self._config, self._register, sorted(regMethods.keys()))
            # self._widget._ui.registerButton.clicked.connect(self._register)
            self._widget._ui.acceptButton.clicked.connect(self._doneExecution)
            self._widget._ui.abortButton.clicked.connect(self._abort)
            self._widget._ui.resetButton.clicked.connect(self._reset)
            self._widget.setModal(True)
            self._setCurrentWidget(self._widget)

        elif self._config['UI Mode']=='False':
            self._register()
            self._doneExecution()

    def _register(self):
        reg = regMethods[self._config['Registration Method']]
        xtol = float(self._config['Min Relative Error'])
        samples = int(self._config['Points to Sample'])
        self.transform, self.sourceDataAligned, (rmse0, self.RMSE) = reg(self.sourceData, self.targetData, xtol=xtol, sample=samples, outputErrors=True)
        print 'Registered...'
        print 'RMSE:', self.RMSE
        print 'T:', self.transform
        return self.transform, self.sourceDataAligned, self.RMSE

    def _abort(self):
        self._doneExecution()
        raise RuntimeError, 'registration aborted'

    def _reset(self):
        self.sourceDataAligned = None
        self.transform = None
        self.RMSE = None

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self.sourceData = dataIn # ju#pointcloud
        else:
            self.targetData = dataIn # ju#pointcloud

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index == 2:
            portData2 = self.sourceDataAligned # ju#pointcloud
            return portData2
        elif index == 3:
            portData3 = self.transform # ju#rigidtransformvector
            return portData3
        else:
            portData4 = self.RMSE # ju#float
            return portData4

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog()
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)
        
        if dlg.exec_():
            self._config = dlg.getConfig()
        
        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self, location):
        '''
        Add code to serialize this step to disk.  The filename should
        use the step identifier (received from getIdentifier()) to keep it
        unique within the workflow.  The suggested name for the file on
        disk is:
            filename = getIdentifier() + '.conf'
        '''
        configuration_file = os.path.join(location, self.getIdentifier() + '.conf')
        conf = QtCore.QSettings(configuration_file, QtCore.QSettings.IniFormat)
        conf.beginGroup('config')
        conf.setValue('identifier', self._config['identifier'])
        conf.setValue('UI Mode', self._config['UI Mode'])
        conf.setValue('Registration Method', self._config['Registration Method'])
        conf.setValue('Min Relative Error', self._config['Min Relative Error'])
        conf.setValue('Points to Sample', self._config['Points to Sample'])
        conf.endGroup()


    def deserialize(self, location):
        '''
        Add code to deserialize this step from disk.  As with the serialize 
        method the filename should use the step identifier.  Obviously the 
        filename used here should be the same as the one used by the
        serialize method.
        '''
        configuration_file = os.path.join(location, self.getIdentifier() + '.conf')
        conf = QtCore.QSettings(configuration_file, QtCore.QSettings.IniFormat)
        conf.beginGroup('config')
        self._config['identifier'] = conf.value('identifier', '')
        self._config['UI Mode'] = conf.value('UI Mode', 'True')
        self._config['Registration Method'] = conf.value('Registration Method', 'Correspondent Rigid')
        self._config['Min Relative Error'] = conf.value('Min Relative Error', '1e-3')
        self._config['Points to Sample'] = conf.value('Points to Sample', '1000')
        conf.endGroup()

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


