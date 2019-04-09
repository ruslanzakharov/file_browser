# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_left.setFont(font)
        self.btn_left.setObjectName("btn_left")
        self.gridLayout.addWidget(self.btn_left, 0, 0, 1, 1)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout.addWidget(self.btn_search, 0, 3, 1, 1)
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_right.setFont(font)
        self.btn_right.setObjectName("btn_right")
        self.gridLayout.addWidget(self.btn_right, 0, 1, 1, 1)
        self.search_field = QtWidgets.QLineEdit(self.centralwidget)
        self.search_field.setMinimumSize(QtCore.QSize(0, 41))
        self.search_field.setText("")
        self.search_field.setObjectName("search_field")
        self.gridLayout.addWidget(self.search_field, 0, 2, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.dir_view = QtWidgets.QTreeView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir_view.sizePolicy().hasHeightForWidth())
        self.dir_view.setSizePolicy(sizePolicy)
        self.dir_view.setBaseSize(QtCore.QSize(0, 0))
        self.dir_view.setRootIsDecorated(True)
        self.dir_view.setObjectName("dir_view")
        self.table_view = QtWidgets.QTreeView(self.splitter)
        self.table_view.setRootIsDecorated(True)
        self.table_view.setExpandsOnDoubleClick(False)
        self.table_view.setObjectName("table_view")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Browser"))
        self.btn_left.setIcon(QtGui.QIcon('files/back.png'))
        self.btn_search.setIcon(QtGui.QIcon('files/search.png'))
        self.btn_right.setIcon(QtGui.QIcon('files/next.png'))
