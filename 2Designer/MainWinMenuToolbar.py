# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinMenuToolbar.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuqw = QtWidgets.QMenu(self.menubar)
        self.menuqw.setObjectName("menuqw")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.menuqw.addSeparator()
        self.menuqw.addSeparator()
        self.menuqw.addAction(self.actionnew)
        self.menuqw.addAction(self.actionopen)
        self.menubar.addAction(self.menuqw.menuAction())
        self.toolBar.addAction(self.actionnew)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuqw.setTitle(_translate("MainWindow", "文件"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionnew.setText(_translate("MainWindow", "NEW"))
        self.actionnew.setToolTip(_translate("MainWindow", "创建新文件"))
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionopen.setText(_translate("MainWindow", "打开"))
        self.actionopen.setToolTip(_translate("MainWindow", "打开文件"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+S"))


