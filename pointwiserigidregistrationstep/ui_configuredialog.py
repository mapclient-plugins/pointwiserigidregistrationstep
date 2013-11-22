# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ju/work_projects/MAP/myplugins/pointwiserigidregistrationstep/pointwiserigidregistrationstep/qt/configuredialog.ui'
#
# Created: Fri Nov 22 15:34:15 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setGeometry(QtCore.QRect(0, 0, 418, 303))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(Dialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label0)
        self.lineEdit0 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName("lineEdit0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit0)
        self.label1 = QtGui.QLabel(self.configGroupBox)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label1)
        self.lineEdit1 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit1.setObjectName("lineEdit1")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit1)
        self.label2 = QtGui.QLabel(self.configGroupBox)
        self.label2.setObjectName("label2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label2)
        self.lineEdit2 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit2.setObjectName("lineEdit2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit2)
        self.label3 = QtGui.QLabel(self.configGroupBox)
        self.label3.setObjectName("label3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label3)
        self.lineEdit3 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit3.setObjectName("lineEdit3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit3)
        self.label4 = QtGui.QLabel(self.configGroupBox)
        self.label4.setObjectName("label4")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label4)
        self.lineEdit4 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit4.setObjectName("lineEdit4")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit4)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "ConfigureDialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("ConfigureDialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("ConfigureDialog", "UI Mode:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("ConfigureDialog", "Registration Method:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("ConfigureDialog", "Min Relatve Error :  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label4.setText(QtGui.QApplication.translate("ConfigureDialog", "Sampling (0-1):  ", None, QtGui.QApplication.UnicodeUTF8))

