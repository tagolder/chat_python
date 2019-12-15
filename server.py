#!/usr/bin/env python
import pika
from PyQt5 import QtWidgets, QtGui
from chatWindow import Ui_chatWindow

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='Dlclient',
                      exchange_type='direct')

channel.queue_declare(queue='client')

clients =  []


def callback(ch, method, properties, body):
    body = body.decode("utf-8")
    print(body)
    if body.find('client')==0:
        for i in clients:
            channel.basic_publish(exchange='',
                            routing_key= body[6:],
                            body='client'+ i)
        clients.append(body[6:])
        for n in clients:
            channel.basic_publish(exchange='',
                            routing_key= n,
                            body='client'+ body[6:])

    elif body.find('[')==0:
        for n in clients:
            channel.basic_publish(exchange='',
                            routing_key= n,
                            body='chat'+ body)
    elif body.find('from=')==0:
        stroka = body[5:]
        nameFrom = stroka[0:stroka.find('+')]
        print(nameFrom)
        stroka  = stroka[stroka.find('+')+4:]
        nameTo = stroka[0:stroka.find('[')]
        print (nameTo)
        stroka = stroka[stroka.find('['):]
        channel.basic_publish(exchange='',
                            routing_key= nameTo,
                            body='lich'+ nameFrom + stroka)
channel.basic_consume(callback,
                      queue='client',
                      no_ack=True)

channel.start_consuming()
'''
class chat(QtWidgets.QMainWindow):
    #model = QtGui.QStandardItemModel()
    
    def __init__(self):
        super(chat, self).__init__()
        self.ui = Ui_chatWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.nameEdit.setText("server")
        self.ui.nameBut.setVisible(False)
        #self.ui.button_send.clicked.connect(self.enterLineClick)
        self.ui.tEdit.setReadOnly(True)
        #app.aboutToQuit.connect(self.Exit)
        #self.ui.listview.clicked.connect(self.UserClick)
        #self.ui.pushButton.clicked.connect(self.PrivatClick)
        self.ui.nameEdit.setReadOnly(True)
        #self.ui.lineedit_you.setReadOnly(True)
        self.ui.msgEdit.setReadOnly(True)
            
            
import sys
app = QtWidgets.QApplication(sys.argv)
window = chat()
window.show()
sys.exit(app.exec_())
'''
