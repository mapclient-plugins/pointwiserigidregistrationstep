# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mayaviregistrationviewerwidget.ui'
#
# Created: Mon Jan 13 23:01:01 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(914, 621)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget1 = QtGui.QWidget(self.widget)
        self.widget1.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtGui.QTableWidget(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.verticalLayout.addWidget(self.tableWidget)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.samplesLineEdit = QtGui.QLineEdit(self.widget1)
        self.samplesLineEdit.setObjectName("samplesLineEdit")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.samplesLineEdit)
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.xtolLineEdit = QtGui.QLineEdit(self.widget1)
        self.xtolLineEdit.setObjectName("xtolLineEdit")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.xtolLineEdit)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.regMethodsComboBox = QtGui.QComboBox(self.widget1)
        self.regMethodsComboBox.setObjectName("regMethodsComboBox")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.regMethodsComboBox)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.registerButton = QtGui.QPushButton(self.widget1)
        self.registerButton.setObjectName("registerButton")
        self.gridLayout_2.addWidget(self.registerButton, 0, 0, 1, 1)
        self.resetButton = QtGui.QPushButton(self.widget1)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout_2.addWidget(self.resetButton, 0, 1, 1, 1)
        self.acceptButton = QtGui.QPushButton(self.widget1)
        self.acceptButton.setObjectName("acceptButton")
        self.gridLayout_2.addWidget(self.acceptButton, 1, 1, 1, 1)
        self.abortButton = QtGui.QPushButton(self.widget1)
        self.abortButton.setObjectName("abortButton")
        self.gridLayout_2.addWidget(self.abortButton, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtGui.QFrame(self.widget1)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.errorGroup = QtGui.QGroupBox(self.widget1)
        self.errorGroup.setObjectName("errorGroup")
        self.formLayout_3 = QtGui.QFormLayout(self.errorGroup)
        self.formLayout_3.setObjectName("formLayout_3")
        self.RMSELineEdit = QtGui.QLineEdit(self.errorGroup)
        self.RMSELineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RMSELineEdit.setReadOnly(True)
        self.RMSELineEdit.setObjectName("RMSELineEdit")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.RMSELineEdit)
        self.RMSELabel = QtGui.QLabel(self.errorGroup)
        self.RMSELabel.setObjectName("RMSELabel")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.RMSELabel)
        self.meanErrorLineEdit = QtGui.QLineEdit(self.errorGroup)
        self.meanErrorLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.meanErrorLineEdit.setReadOnly(True)
        self.meanErrorLineEdit.setObjectName("meanErrorLineEdit")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.meanErrorLineEdit)
        self.SDLineEdit = QtGui.QLineEdit(self.errorGroup)
        self.SDLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SDLineEdit.setReadOnly(True)
        self.SDLineEdit.setObjectName("SDLineEdit")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.SDLineEdit)
        self.meanErrorLabel = QtGui.QLabel(self.errorGroup)
        self.meanErrorLabel.setObjectName("meanErrorLabel")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.meanErrorLabel)
        self.SDLabel = QtGui.QLabel(self.errorGroup)
        self.SDLabel.setObjectName("SDLabel")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.SDLabel)
        self.verticalLayout.addWidget(self.errorGroup)
        self.screenshotgroup = QtGui.QGroupBox(self.widget1)
        self.screenshotgroup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.screenshotgroup.setObjectName("screenshotgroup")
        self.formLayout = QtGui.QFormLayout(self.screenshotgroup)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.pixelsXLabel = QtGui.QLabel(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelsXLabel.sizePolicy().hasHeightForWidth())
        self.pixelsXLabel.setSizePolicy(sizePolicy)
        self.pixelsXLabel.setObjectName("pixelsXLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pixelsXLabel)
        self.screenshotPixelXLineEdit = QtGui.QLineEdit(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotPixelXLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelXLineEdit.setSizePolicy(sizePolicy)
        self.screenshotPixelXLineEdit.setObjectName("screenshotPixelXLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.screenshotPixelXLineEdit)
        self.pixelsYLabel = QtGui.QLabel(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelsYLabel.sizePolicy().hasHeightForWidth())
        self.pixelsYLabel.setSizePolicy(sizePolicy)
        self.pixelsYLabel.setObjectName("pixelsYLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pixelsYLabel)
        self.screenshotPixelYLineEdit = QtGui.QLineEdit(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotPixelYLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelYLineEdit.setSizePolicy(sizePolicy)
        self.screenshotPixelYLineEdit.setObjectName("screenshotPixelYLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.screenshotPixelYLineEdit)
        self.screenshotFilenameLabel = QtGui.QLabel(self.screenshotgroup)
        self.screenshotFilenameLabel.setObjectName("screenshotFilenameLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.screenshotFilenameLabel)
        self.screenshotFilenameLineEdit = QtGui.QLineEdit(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotFilenameLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotFilenameLineEdit.setSizePolicy(sizePolicy)
        self.screenshotFilenameLineEdit.setObjectName("screenshotFilenameLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.screenshotFilenameLineEdit)
        self.screenshotSaveButton = QtGui.QPushButton(self.screenshotgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotSaveButton.sizePolicy().hasHeightForWidth())
        self.screenshotSaveButton.setSizePolicy(sizePolicy)
        self.screenshotSaveButton.setObjectName("screenshotSaveButton")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.screenshotSaveButton)
        self.verticalLayout.addWidget(self.screenshotgroup)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.widget1, 0, 0, 1, 1)
        self.MayaviScene = MayaviSceneWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MayaviScene.sizePolicy().hasHeightForWidth())
        self.MayaviScene.setSizePolicy(sizePolicy)
        self.MayaviScene.setObjectName("MayaviScene")
        self.gridLayout.addWidget(self.MayaviScene, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Point to Point Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Visible", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Samples:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Min Rel Err:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Reg Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.registerButton.setText(QtGui.QApplication.translate("Dialog", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("Dialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.acceptButton.setText(QtGui.QApplication.translate("Dialog", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.abortButton.setText(QtGui.QApplication.translate("Dialog", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.errorGroup.setTitle(QtGui.QApplication.translate("Dialog", "Registration Errors", None, QtGui.QApplication.UnicodeUTF8))
        self.RMSELabel.setText(QtGui.QApplication.translate("Dialog", "RMS:", None, QtGui.QApplication.UnicodeUTF8))
        self.meanErrorLabel.setText(QtGui.QApplication.translate("Dialog", "Mean:", None, QtGui.QApplication.UnicodeUTF8))
        self.SDLabel.setText(QtGui.QApplication.translate("Dialog", "S.D.:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotgroup.setTitle(QtGui.QApplication.translate("Dialog", "Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelsXLabel.setText(QtGui.QApplication.translate("Dialog", "Pixels X:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotPixelXLineEdit.setText(QtGui.QApplication.translate("Dialog", "800", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelsYLabel.setText(QtGui.QApplication.translate("Dialog", "Pixels Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotPixelYLineEdit.setText(QtGui.QApplication.translate("Dialog", "600", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotFilenameLabel.setText(QtGui.QApplication.translate("Dialog", "Filename:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotFilenameLineEdit.setText(QtGui.QApplication.translate("Dialog", "screenshot.png", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotSaveButton.setText(QtGui.QApplication.translate("Dialog", "Save Screenshot", None, QtGui.QApplication.UnicodeUTF8))

from mappluginutils.mayaviviewer import MayaviSceneWidget
