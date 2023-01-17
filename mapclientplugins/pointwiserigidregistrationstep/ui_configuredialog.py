# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(436, 393)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label1)

        self.UICheckBox = QCheckBox(self.configGroupBox)
        self.UICheckBox.setObjectName(u"UICheckBox")
        self.UICheckBox.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.UICheckBox)

        self.label2 = QLabel(self.configGroupBox)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label2)

        self.regMethodsComboBox = QComboBox(self.configGroupBox)
        self.regMethodsComboBox.setObjectName(u"regMethodsComboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.regMethodsComboBox)

        self.label3 = QLabel(self.configGroupBox)
        self.label3.setObjectName(u"label3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label3)

        self.xtolLineEdit = QLineEdit(self.configGroupBox)
        self.xtolLineEdit.setObjectName(u"xtolLineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.xtolLineEdit)

        self.label4 = QLabel(self.configGroupBox)
        self.label4.setObjectName(u"label4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label4)

        self.sampleLineEdit = QLineEdit(self.configGroupBox)
        self.sampleLineEdit.setObjectName(u"sampleLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.sampleLineEdit)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.configGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.configGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_3)

        self.sLineEdit = QLineEdit(self.configGroupBox)
        self.sLineEdit.setObjectName(u"sLineEdit")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.sLineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.configGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.txLineEdit = QLineEdit(self.configGroupBox)
        self.txLineEdit.setObjectName(u"txLineEdit")

        self.horizontalLayout_2.addWidget(self.txLineEdit)

        self.label_5 = QLabel(self.configGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.tyLineEdit = QLineEdit(self.configGroupBox)
        self.tyLineEdit.setObjectName(u"tyLineEdit")

        self.horizontalLayout_2.addWidget(self.tyLineEdit)

        self.label_6 = QLabel(self.configGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.tzLineEdit = QLineEdit(self.configGroupBox)
        self.tzLineEdit.setObjectName(u"tzLineEdit")

        self.horizontalLayout_2.addWidget(self.tzLineEdit)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.configGroupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.rxLineEdit = QLineEdit(self.configGroupBox)
        self.rxLineEdit.setObjectName(u"rxLineEdit")

        self.horizontalLayout_3.addWidget(self.rxLineEdit)

        self.label_8 = QLabel(self.configGroupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.ryLineEdit = QLineEdit(self.configGroupBox)
        self.ryLineEdit.setObjectName(u"ryLineEdit")

        self.horizontalLayout_3.addWidget(self.ryLineEdit)

        self.label_9 = QLabel(self.configGroupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.rzLineEdit = QLineEdit(self.configGroupBox)
        self.rzLineEdit.setObjectName(u"rzLineEdit")

        self.horizontalLayout_3.addWidget(self.rzLineEdit)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configure Dialog", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("Dialog", u"identifier:  ", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"UI Mode:  ", None))
        self.UICheckBox.setText("")
        self.label2.setText(QCoreApplication.translate("Dialog", u"Registration Method:  ", None))
        self.label3.setText(QCoreApplication.translate("Dialog", u"Min Relatve Error:  ", None))
        self.label4.setText(QCoreApplication.translate("Dialog", u"Points to Sample:", None))
        self.sampleLineEdit.setInputMask("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Initial Translation:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Initial Rotation:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Initial Scale:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"y", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"z", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"y", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"z", None))
    # retranslateUi

