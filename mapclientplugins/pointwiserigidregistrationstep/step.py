'''
MAP Client Plugin Step
'''
from PySide6 import QtGui
import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.pointwiserigidregistrationstep.configuredialog import ConfigureDialog

from gias3.registration import alignment_fitting as AF
from gias3.common import transform3D
from mapclientplugins.pointwiserigidregistrationstep.mayaviregistrationviewerwidget import \
    MayaviRegistrationViewerWidget
from gias3.mapclientpluginutilities.datatypes import transformations as T

import numpy as np

regMethods = {
    'Correspondent Rigid': AF.fitRigid,
    'Correspondent Rigid+Scale': AF.fitRigidScale,
    'Correspondent Affine': AF.fitAffine,
    'ICP Rigid Source-Target': AF.fitDataRigidEPDP,
    'ICP Rigid Target-Source': AF.fitDataRigidDPEP,
    'ICP Rigid+Scale Source-Target': AF.fitDataRigidScaleEPDP,
    'ICP Rigid+Scale Target-Source': AF.fitDataRigidScaleDPEP,
}

regMethodTransforms = {
    'Correspondent Rigid': T.RigidTransformAboutPoint,
    'Correspondent Rigid+Scale': T.RigidScaleTransformAboutPoint,
    'Correspondent Affine': T.AffineTransform,
    'ICP Rigid Source-Target': T.RigidTransformAboutPoint,
    'ICP Rigid Target-Source': T.RigidTransformAboutPoint,
    'ICP Rigid+Scale Source-Target': T.RigidScaleTransformAboutPoint,
    'ICP Rigid+Scale Target-Source': T.RigidScaleTransformAboutPoint,
}


class PointWiseRigidRegistrationStep(WorkflowStepMountPoint):
    '''
    Step for rigid-body and scaling registration of 2 point clouds.
    '''

    def __init__(self, location):
        super(PointWiseRigidRegistrationStep, self).__init__('Point-wise Rigid Registration', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Registration'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/pointwiserigidregistrationstep/images/pointwiserigidregicon.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud'))  # source
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud'))  # target
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#geometrictransform'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'python#float'))
        self._config = {}
        self._config['identifier'] = ''
        self._config['UI Mode'] = True
        self._config['Registration Method'] = 'Correspondent Affine'
        self._config['Min Relative Error'] = '1e-3'
        self._config['Points to Sample'] = '1000'
        self._config['Init Trans'] = [0.0, 0.0, 0.0]
        self._config['Init Rot'] = [0.0, 0.0, 0.0]
        self._config['Init Scale'] = 1.0

        self.sourceData = None
        self.targetData = None
        self.sourceDataAligned = None
        self.transform = None
        self.RMSE = -1.0

        self._widget = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        if self._config['UI Mode']:
            self._widget = MayaviRegistrationViewerWidget(
                self.sourceData, self.targetData, self._config,
                self._register, sorted(regMethods.keys()),
                self._manualTransform
            )
            self._widget._ui.acceptButton.clicked.connect(self._doneExecution)
            self._widget._ui.abortButton.clicked.connect(self._abort)
            self._widget._ui.resetButton.clicked.connect(self._reset)
            self._setCurrentWidget(self._widget)
        else:
            self._register()
            self._doneExecution()

    def _makeX0(self):
        t0 = self._config['Init Trans']
        r0 = [np.deg2rad(x) for x in self._config['Init Rot']]
        s0 = self._config['Init Scale']

        # auto initialise translation
        if t0 == [0, 0, 0]:
            t0 = self.targetData.mean(0) - self.sourceData.mean(0)

        print('t0, r0, s0:', t0, r0, s0)

        reg = self._config['Registration Method']
        if reg == 'Correspondent Affine':
            return None
        elif 'Rigid+Scale' in reg:
            return np.hstack([t0, r0, s0])
        elif 'Rigid' in reg:
            return np.hstack([t0, r0])
        else:
            return None

    def _manualTransform(self):
        t0 = self._config['Init Trans']
        r0 = [np.deg2rad(x) for x in self._config['Init Rot']]
        s0 = self._config['Init Scale']

        print('t0, r0, s0:', t0, r0, s0)

        # apply transform to source points
        T = np.hstack([t0, r0, s0])
        self.sourceDataAligned = transform3D.transformRigidScale3DAboutCoM(self.sourceData, T)
        self.transform = regMethodTransforms[self._config['Registration Method']](T)
        self.transform.setP(self.sourceData.mean(0))
        return self.transform, self.sourceDataAligned

    def _register(self):
        reg = regMethods[self._config['Registration Method']]
        xtol = float(self._config['Min Relative Error'])
        samples = int(self._config['Points to Sample'])
        x0 = self._makeX0()
        print('T0:', x0)
        if x0 is None:
            T, self.sourceDataAligned, \
            (rmse0, self.RMSE) = reg(self.sourceData, self.targetData, xtol=xtol,
                                     sample=samples, output_errors=True)
        else:
            T, self.sourceDataAligned, \
            (rmse0, self.RMSE) = reg(self.sourceData, self.targetData, t0=x0, xtol=xtol,
                                     sample=samples, output_errors=True)

        self.transform = regMethodTransforms[self._config['Registration Method']](T)
        if self._config['Registration Method'] != 'Correspondent Affine':
            self.transform.setP(self.sourceData.mean(0))

        print('Registered...')
        print('RMSE:', self.RMSE)
        print('T:', T)
        return self.transform, self.sourceDataAligned, self.RMSE

    def _abort(self):
        # self._doneExecution()
        raise RuntimeError('registration aborted')

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
            self.sourceData = np.array(dataIn, dtype=float)  # ju#pointcloud
        else:
            self.targetData = np.array(dataIn, dtype=float)  # ju#pointcloud

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index == 2:
            portData2 = self.sourceDataAligned  # ju#pointcloud
            return portData2.tolist()
        elif index == 3:
            portData3 = self.transform  # ju#rigidtransformvector
            return portData3
        else:
            portData4 = self.RMSE  # ju#float
            return portData4

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog(sorted(regMethods.keys()), self._main_window)
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

    def serialize(self):
        '''
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        '''
        self._config.update(json.loads(string))
        self._parseLegacyParams()

        d = ConfigureDialog(sorted(regMethods.keys()))
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()

    def _parseLegacyParams(self):
        """Turn strs of lists into lists in config
        """

        def _parseStrList(s):
            _s1 = s[1:-1]
            return [float(x) for x in _s1.split(',')]

        if isinstance(self._config['Init Trans'], str):
            self._config['Init Trans'] = _parseStrList(self._config['Init Trans'])

        if isinstance(self._config['Init Rot'], str):
            self._config['Init Rot'] = _parseStrList(self._config['Init Rot'])

        if isinstance(self._config['Init Scale'], str):
            self._config['Init Scale'] = float(self._config['Init Scale'])
