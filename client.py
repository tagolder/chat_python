#!/usr/bin/env python
import pika
from PyQt5 import QtWidgets,QtGui, QtCore
from PyQt5.QtWidgets import QFormLayout, QLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import QModelIndex
from chatWindow import Ui_chatWindow
import threading
import re
from datetime import datetime, date, time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
#channel.queue_declare('osn')
channellich = connection.channel()

model = QtGui.QStandardItemModel()
class chat(QtWidgets.QMainWindow):
    def NameButClick(self):
        
        channellich.queue_declare(queue=self.ui.nameEdit.text())
        print(self.ui.nameEdit.text())
        if self.ui.nameEdit.text() != "":
            self.ui.nameBut.setVisible(False)
            channel.basic_publish(exchange='',
                      routing_key='client',
                      body= 'client'+self.ui.nameEdit.text())
            thr = threading.Thread(target=self.cc, args=(True,))
            thr.daemon = True
            thr.start()
    def cc(self, checks):
        
        def callback(ch, method, properties, body):
            body = body.decode("utf-8")
            print (body)
            
            if body.find('client') == 0 :
                item = QtGui.QStandardItem(body[6:])
                model.appendRow(item)
                self.ui.listView.setModel(model)
            elif body.find('chat')==0:
                self.ui.tEdit.append(body[4:])
            elif body.find('lich')==0:
                nameFrom = body[4:body.find('[')]
                stroka =  body[body.find('['):]
                
                ind = self.ui.tabWidget.indexOf(self.ui.tabWidget.findChild(QtWidgets.QWidget, nameFrom))
                print (ind)
                if ind != -1:
                    self.ui.tabWidget.setCurrentIndex(ind)
                    tEdit = self.ui.tabWidget.currentWidget().findChild(QtWidgets.QTextEdit,"Edit")
                    tEdit.append(stroka)

            
        channellich.basic_consume(callback,
                      queue=self.ui.nameEdit.text(),
                      no_ack=True)        
        channellich.start_consuming()
        connection.close()
        
    def userClick(self, index = QModelIndex()):
        self.Index = index
        tabPol = QtWidgets.QWidget()
        tabPol.setObjectName(index.data())
        Edit = QtWidgets.QTextEdit(tabPol)
        Edit.setGeometry(QtCore.QRect(0, 10, 501, 461))
        Edit.setReadOnly(True)
        Edit.setObjectName("Edit")
        if index.data() != self.ui.nameEdit.text():
            ind = self.ui.tabWidget.indexOf(self.ui.tabWidget.findChild(QtWidgets.QWidget, index.data()))
            if  ind == -1:
                inde = self.ui.tabWidget.addTab(tabPol, index.data())
                self.ui.tabWidget.setCurrentIndex(inde)
            else:
                self.ui.tabWidget.setCurrentIndex(ind)
    def otprClick(self):
        print('индекс')
        print (self.ui.tabWidget.currentIndex())
        if self.ui.tabWidget.currentIndex() == 0:
            channel.basic_publish(exchange='',
                          routing_key= 'client',
                          body= '[' + str(datetime.now(tz=None))+ '] ' + self.ui.nameEdit.text() + ': '+ self.ui.msgEdit.text())
        else:
            W = self.ui.tabWidget.currentWidget()
            stroka = W.objectName()
            print ('имя')
            print(W.objectName())
            channel.basic_publish(exchange='',
                          routing_key= 'client',
                          body= 'from='+self.ui.nameEdit.text()+'+to='+stroka+'[' + str(datetime.now(tz=None))+ '] ' + self.ui.nameEdit.text() + ': '+ self.ui.msgEdit.text())

        self.ui.msgEdit.setText("")
    def openHelp(self):
        print("fsasdfasda")
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("help")
        tEdit = QtWidgets.QTextEdit(dialog)
        tEdit.setPlainText("")
        layout = QFormLayout()
        layout.addWidget(tEdit)
        dialog.setMinimumSize(300,100)
        dialog.setLayout(layout)
        print("asdasda")
        dialog.exec_()
        
        
    def skrDialog(self):
        nameDial = self.Index.data()
        ind = self.ui.tabWidget.indexOf(self.ui.tabWidget.findChild(QtWidgets.QWidget, nameDial))
        self.ui.tabWidget.removeTab(ind)
    def __init__(self):
        super(chat, self).__init__()
        self.ui = Ui_chatWindow()
        self.ui.setupUi(self)
        self.ui.listView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        skr = QtWidgets.QAction("Скрыть диалог", self)
        skr.triggered.connect(self.skrDialog)
        self.ui.listView.addAction(skr)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.msgBut.clicked.connect(self.otprClick)
        self.ui.nameBut.clicked.connect(self.NameButClick)
        self.ui.tEdit.setReadOnly(True)
        self.ui.listView.clicked.connect(self.userClick)
        self.ui.nameEdit.setReadOnly(False)
        self.Index = QModelIndex()
        self.ui.actionHelp.triggered.connect(self.openHelp) 


        
import sys
app = QtWidgets.QApplication(sys.argv)
window = chat()
window.setWindowTitle("Здесь могла бы быть ваша реклама")

window.show()
sys.exit(app.exec_())
   
