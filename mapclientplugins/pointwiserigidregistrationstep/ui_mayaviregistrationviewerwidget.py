# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mayaviregistrationviewerwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from gias3.mapclientpluginutilities.viewers.mayaviscenewidget import MayaviSceneWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1145, 804)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widgetMain = QWidget(Dialog)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widgetMain.sizePolicy().hasHeightForWidth())
        self.widgetMain.setSizePolicy(sizePolicy)
        self.widgetMain.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.widgetMain)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.widgetMain)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 150))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout.addWidget(self.tableWidget)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.regMethodsComboBox = QComboBox(self.widget)
        self.regMethodsComboBox.setObjectName(u"regMethodsComboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.regMethodsComboBox)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.xtolLineEdit = QLineEdit(self.widget)
        self.xtolLineEdit.setObjectName(u"xtolLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.xtolLineEdit)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label)

        self.samplesLineEdit = QLineEdit(self.widget)
        self.samplesLineEdit.setObjectName(u"samplesLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.samplesLineEdit)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.initRotLayout = QHBoxLayout()
        self.initRotLayout.setObjectName(u"initRotLayout")
        self.doubleSpinBox_rotx = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_rotx.setObjectName(u"doubleSpinBox_rotx")
        self.doubleSpinBox_rotx.setMinimum(-360.000000000000000)
        self.doubleSpinBox_rotx.setMaximum(360.000000000000000)

        self.initRotLayout.addWidget(self.doubleSpinBox_rotx)

        self.doubleSpinBox_roty = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_roty.setObjectName(u"doubleSpinBox_roty")
        self.doubleSpinBox_roty.setMinimum(-360.000000000000000)
        self.doubleSpinBox_roty.setMaximum(360.000000000000000)

        self.initRotLayout.addWidget(self.doubleSpinBox_roty)

        self.doubleSpinBox_rotz = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_rotz.setObjectName(u"doubleSpinBox_rotz")
        self.doubleSpinBox_rotz.setMinimum(-360.000000000000000)
        self.doubleSpinBox_rotz.setMaximum(360.000000000000000)

        self.initRotLayout.addWidget(self.doubleSpinBox_rotz)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.initRotLayout)

        self.initTransLayout = QHBoxLayout()
        self.initTransLayout.setObjectName(u"initTransLayout")
        self.doubleSpinBox_tx = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_tx.setObjectName(u"doubleSpinBox_tx")
        self.doubleSpinBox_tx.setMinimum(-100000.000000000000000)
        self.doubleSpinBox_tx.setMaximum(100000.000000000000000)
        self.doubleSpinBox_tx.setSingleStep(1.000000000000000)

        self.initTransLayout.addWidget(self.doubleSpinBox_tx)

        self.doubleSpinBox_ty = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_ty.setObjectName(u"doubleSpinBox_ty")
        self.doubleSpinBox_ty.setMinimum(-100000.000000000000000)
        self.doubleSpinBox_ty.setMaximum(100000.000000000000000)

        self.initTransLayout.addWidget(self.doubleSpinBox_ty)

        self.doubleSpinBox_tz = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_tz.setObjectName(u"doubleSpinBox_tz")
        self.doubleSpinBox_tz.setMinimum(-100000.000000000000000)
        self.doubleSpinBox_tz.setMaximum(100000.000000000000000)

        self.initTransLayout.addWidget(self.doubleSpinBox_tz)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.initTransLayout)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.doubleSpinBox_scale = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_scale.setObjectName(u"doubleSpinBox_scale")
        self.doubleSpinBox_scale.setMinimum(-100000.000000000000000)
        self.doubleSpinBox_scale.setMaximum(100000.000000000000000)
        self.doubleSpinBox_scale.setSingleStep(0.050000000000000)
        self.doubleSpinBox_scale.setValue(1.000000000000000)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBox_scale)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.registerButton = QPushButton(self.widget)
        self.registerButton.setObjectName(u"registerButton")

        self.gridLayout_2.addWidget(self.registerButton, 0, 0, 1, 1)

        self.resetButton = QPushButton(self.widget)
        self.resetButton.setObjectName(u"resetButton")

        self.gridLayout_2.addWidget(self.resetButton, 0, 1, 1, 1)

        self.acceptButton = QPushButton(self.widget)
        self.acceptButton.setObjectName(u"acceptButton")

        self.gridLayout_2.addWidget(self.acceptButton, 1, 1, 1, 1)

        self.abortButton = QPushButton(self.widget)
        self.abortButton.setObjectName(u"abortButton")

        self.gridLayout_2.addWidget(self.abortButton, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.errorGroup = QGroupBox(self.widget)
        self.errorGroup.setObjectName(u"errorGroup")
        self.formLayout_3 = QFormLayout(self.errorGroup)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.RMSELineEdit = QLineEdit(self.errorGroup)
        self.RMSELineEdit.setObjectName(u"RMSELineEdit")
        self.RMSELineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.RMSELineEdit.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.RMSELineEdit)

        self.RMSELabel = QLabel(self.errorGroup)
        self.RMSELabel.setObjectName(u"RMSELabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.RMSELabel)

        self.meanErrorLineEdit = QLineEdit(self.errorGroup)
        self.meanErrorLineEdit.setObjectName(u"meanErrorLineEdit")
        self.meanErrorLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.meanErrorLineEdit.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.meanErrorLineEdit)

        self.SDLineEdit = QLineEdit(self.errorGroup)
        self.SDLineEdit.setObjectName(u"SDLineEdit")
        self.SDLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SDLineEdit.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.SDLineEdit)

        self.meanErrorLabel = QLabel(self.errorGroup)
        self.meanErrorLabel.setObjectName(u"meanErrorLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.meanErrorLabel)

        self.SDLabel = QLabel(self.errorGroup)
        self.SDLabel.setObjectName(u"SDLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.SDLabel)


        self.verticalLayout.addWidget(self.errorGroup)

        self.screenshotgroup = QGroupBox(self.widget)
        self.screenshotgroup.setObjectName(u"screenshotgroup")
        self.screenshotgroup.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout = QFormLayout(self.screenshotgroup)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.pixelsXLabel = QLabel(self.screenshotgroup)
        self.pixelsXLabel.setObjectName(u"pixelsXLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pixelsXLabel.sizePolicy().hasHeightForWidth())
        self.pixelsXLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pixelsXLabel)

        self.screenshotPixelXLineEdit = QLineEdit(self.screenshotgroup)
        self.screenshotPixelXLineEdit.setObjectName(u"screenshotPixelXLineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.screenshotPixelXLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelXLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.screenshotPixelXLineEdit)

        self.pixelsYLabel = QLabel(self.screenshotgroup)
        self.pixelsYLabel.setObjectName(u"pixelsYLabel")
        sizePolicy2.setHeightForWidth(self.pixelsYLabel.sizePolicy().hasHeightForWidth())
        self.pixelsYLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pixelsYLabel)

        self.screenshotPixelYLineEdit = QLineEdit(self.screenshotgroup)
        self.screenshotPixelYLineEdit.setObjectName(u"screenshotPixelYLineEdit")
        sizePolicy3.setHeightForWidth(self.screenshotPixelYLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelYLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.screenshotPixelYLineEdit)

        self.screenshotFilenameLabel = QLabel(self.screenshotgroup)
        self.screenshotFilenameLabel.setObjectName(u"screenshotFilenameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.screenshotFilenameLabel)

        self.screenshotFilenameLineEdit = QLineEdit(self.screenshotgroup)
        self.screenshotFilenameLineEdit.setObjectName(u"screenshotFilenameLineEdit")
        sizePolicy3.setHeightForWidth(self.screenshotFilenameLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotFilenameLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.screenshotFilenameLineEdit)

        self.screenshotSaveButton = QPushButton(self.screenshotgroup)
        self.screenshotSaveButton.setObjectName(u"screenshotSaveButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.screenshotSaveButton.sizePolicy().hasHeightForWidth())
        self.screenshotSaveButton.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.screenshotSaveButton)


        self.verticalLayout.addWidget(self.screenshotgroup)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.MayaviScene = MayaviSceneWidget(self.widgetMain)
        self.MayaviScene.setObjectName(u"MayaviScene")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.MayaviScene.sizePolicy().hasHeightForWidth())
        self.MayaviScene.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.MayaviScene, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.widgetMain)

        QWidget.setTabOrder(self.tableWidget, self.regMethodsComboBox)
        QWidget.setTabOrder(self.regMethodsComboBox, self.xtolLineEdit)
        QWidget.setTabOrder(self.xtolLineEdit, self.samplesLineEdit)
        QWidget.setTabOrder(self.samplesLineEdit, self.registerButton)
        QWidget.setTabOrder(self.registerButton, self.resetButton)
        QWidget.setTabOrder(self.resetButton, self.abortButton)
        QWidget.setTabOrder(self.abortButton, self.acceptButton)
        QWidget.setTabOrder(self.acceptButton, self.RMSELineEdit)
        QWidget.setTabOrder(self.RMSELineEdit, self.meanErrorLineEdit)
        QWidget.setTabOrder(self.meanErrorLineEdit, self.SDLineEdit)
        QWidget.setTabOrder(self.SDLineEdit, self.screenshotPixelXLineEdit)
        QWidget.setTabOrder(self.screenshotPixelXLineEdit, self.screenshotPixelYLineEdit)
        QWidget.setTabOrder(self.screenshotPixelYLineEdit, self.screenshotFilenameLineEdit)
        QWidget.setTabOrder(self.screenshotFilenameLineEdit, self.screenshotSaveButton)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Point to Point Registration", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Visible", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Type", None));
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Reg. Method:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Min Rel Err:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Samples:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Translations.:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Rotations:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Scaling:", None))
        self.registerButton.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.resetButton.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.acceptButton.setText(QCoreApplication.translate("Dialog", u"Accept", None))
        self.abortButton.setText(QCoreApplication.translate("Dialog", u"Abort", None))
        self.errorGroup.setTitle(QCoreApplication.translate("Dialog", u"Registration Errors", None))
        self.RMSELabel.setText(QCoreApplication.translate("Dialog", u"RMS:", None))
        self.meanErrorLabel.setText(QCoreApplication.translate("Dialog", u"Mean:", None))
        self.SDLabel.setText(QCoreApplication.translate("Dialog", u"S.D.:", None))
        self.screenshotgroup.setTitle(QCoreApplication.translate("Dialog", u"Screenshot", None))
        self.pixelsXLabel.setText(QCoreApplication.translate("Dialog", u"Pixels X:", None))
        self.screenshotPixelXLineEdit.setText(QCoreApplication.translate("Dialog", u"800", None))
        self.pixelsYLabel.setText(QCoreApplication.translate("Dialog", u"Pixels Y:", None))
        self.screenshotPixelYLineEdit.setText(QCoreApplication.translate("Dialog", u"600", None))
        self.screenshotFilenameLabel.setText(QCoreApplication.translate("Dialog", u"Filename:", None))
        self.screenshotFilenameLineEdit.setText(QCoreApplication.translate("Dialog", u"screenshot.png", None))
        self.screenshotSaveButton.setText(QCoreApplication.translate("Dialog", u"Save Screenshot", None))
    # retranslateUi

