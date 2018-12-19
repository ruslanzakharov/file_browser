# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 57)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.input = QtWidgets.QLineEdit(Dialog)
        self.input.setObjectName("input")
        self.gridLayout.addWidget(self.input, 0, 0, 1, 1)
        self.create = QtWidgets.QPushButton(Dialog)
        self.create.setObjectName("create")
        self.gridLayout.addWidget(self.create, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новая папка"))
        self.create.setText(_translate("Dialog", "Создать"))

