# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_chatWindow(object):
    def setupUi(self, chatWindow):
        chatWindow.setObjectName("chatWindow")
        chatWindow.resize(935, 600)
        self.centralwidget = QtWidgets.QWidget(chatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(150, 10, 500, 510))
        self.tabWidget.setObjectName("tabWidget")
        self.osn = QtWidgets.QWidget()
        self.osn.setObjectName("osn")
        self.tEdit = QtWidgets.QTextEdit(self.osn)
        self.tEdit.setGeometry(QtCore.QRect(0, 10, 501, 461))
        self.tEdit.setReadOnly(True)
        self.tEdit.setObjectName("tEdit")
        self.msgEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.msgEdit.setGeometry(QtCore.QRect(150, 521, 320, 27))
        self.msgEdit.setObjectName("msgEdit")
        self.msgBut = QtWidgets.QPushButton(self.centralwidget)
        self.msgBut.setGeometry(QtCore.QRect(470, 521, 180, 27))
        self.msgBut.setObjectName("msgBut")
        self.tabWidget.addTab(self.osn, "Общий")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(660, 50, 270, 500))
        self.listView.setObjectName("listView")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(10, 80, 131, 27))
        self.nameEdit.setObjectName("nameEdit")
        self.nameBut = QtWidgets.QPushButton(self.centralwidget)
        self.nameBut.setGeometry(QtCore.QRect(25, 120, 100, 27))
        self.nameBut.setObjectName("nameBut")
        chatWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chatWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")


        self.actionAbout = QtWidgets.QAction(chatWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(chatWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())


        chatWindow.setMenuBar(self.menubar)

        self.retranslateUi(chatWindow)
        QtCore.QMetaObject.connectSlotsByName(chatWindow)

    def retranslateUi(self, chatWindow):
        _translate = QtCore.QCoreApplication.translate
        chatWindow.setWindowTitle(_translate("chatWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.osn), _translate("chatWindow", "Общий"))
        self.nameBut.setText(_translate("chatWindow", "войти"))
        #self.menuAbout.setTitle(_translate("chatWindow", "about"))
        self.menuFile.setTitle(_translate("chatWindow", "File"))
