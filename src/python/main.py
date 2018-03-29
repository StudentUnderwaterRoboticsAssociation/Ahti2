import os
import interface
from PyQt4 import*
from PyQt4.QtCore import*
from PyQt4.QtGui import*
from PyQt4.QtCore import QThread
import time
import threading
import thread
import SocketServer
import socket
try:
    import qdarkstyle
    os.system("clear")
except:
    print "Dark Stylesheet not found. Installing it..."
    os.system("clr")
    os.system("pip install qdarkstyle")

import sys
os.system("pyuic4 -o interface.py interface.ui")


class ThreadedTCPServer(SocketServer.TCPServer):
    pass





class App(QtGui.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, parent = None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.keepRunning = True
        self.serverState = False
        self.commandList= []
    
    def run(self):
        self.pbSet = [self.progressBar, self.progressBar_2, self.progressBar_3, self.progressBar_4]
        self.hSlider = [self.horizontalSlider, self.horizontalSlider_2, self.horizontalSlider_3, self.horizontalSlider_4]
        for x in range(0, 4):
            self.pbSet[x].reset()
            self.hSlider[x].setRange(0, 180)
        self.horizontalSlider.valueChanged.connect(self.openGripper)
        self.horizontalSlider_2.valueChanged.connect(self.rotateGripper)
        self.horizontalSlider_3.valueChanged.connect(self.panCamera)
        self.horizontalSlider_4.valueChanged.connect(self.ledsBrightness)
        
        #defaults
        self.horizontalSlider_4.setEnabled(False)
        self.progressBar.setRange(0, 180)
        self.progressBar_2.setRange(0, 180)
        self.progressBar_3.setRange(0, 180)
        self.progressBar_4.setRange(0, 180)
        self.pushButton_15.autoDefault()
        self.tabWidget.setTabText(0,"Rover")
        self.tabWidget.setTabText(1, "Network")
        
        #inflation gripper control
        self.pushButton_15.toggle()
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.clicked.connect(self.inflationGripper)

        #Led control
        self.pushButton_5.toggle()
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.clicked.connect(self.ledControl)
        

        #rotation gripper control
        self.pushButton_4.pressed.connect(self.rotateClockwise)
        self.pushButton_3.pressed.connect(self.rotateAntiClockwise)

        self.lineEdit.setText('192.168.1.100')
        self.lineEdit_2.setText('4242')
        # t1 = threading.Thread(target = self.pushButton.clicked.connect(self.startServer))
        # t1.daemon = True
        # t1.start()
        self.pushButton.clicked.connect(self.startServer)
        self.pushButton_2.clicked.connect(self.shutServer)
        self.pushButton_7.clicked.connect(self.resetConnection)
        self.pushButton_9.clicked.connect(self.sendData)

    def resetConnection(self):
        
        print ("Server Restart Initiated")
        self.shutServer()
        #self.t1.join()
        time.sleep(2)
        self.startServer()

    def shutServer(self):
        self.keepRunning = False

    def core(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address = ('192.168.1.100', 4242)
        sock.connect(server_address)
        sock.sendall(str(self.lineEdit_3.text()))
        data = sock.recv(100)
        print data
        sock.close()
            
           
    def startServer(self):
        self.t1 = threading.Thread(target = self.core)
        self.t1.daemon = True
        self.t1.start()

        #self.connection.close()
    def sendData(self, connectionObject):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address = ('192.168.1.100', 4242)
        sock.connect(server_address)
        sock.sendall(str(self.lineEdit_3.text()))
        data = sock.recv(100)
        print data
        sock.close()


    def rotateClockwise(self):
        print "ClockWise"
    def rotateAntiClockwise(self):
        print "Anti ClockWise"
    def openGripper(self, x):
        self.progressBar.setValue(x)
    def rotateGripper(self,x):
        self.progressBar_2.setValue(x)
    def panCamera(self, x):
        self.progressBar_3.setValue(x)
    def ledsBrightness(self, x):
        self.progressBar_4.setValue(x)
    def inflationGripper(self):
        if self.pushButton_15.isChecked():
            print "Open"
            self.pushButton_15.setText("Open")
        else:
            print "Close"
            self.pushButton_15.setText("Close")
    def ledControl(self):
        if self.pushButton_5.isChecked():
            print "Off"
            self.horizontalSlider_4.setEnabled(False)
            self.pushButton_5.setText("Off")        
        else:
            print "On"
            self.horizontalSlider_4.setEnabled(True)
            self.pushButton_5.setText("On")

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
    form = App()
    form.run()
    form.show()
    app.exec_()


class requestHandler(SocketServer.BaseRequestHandler):
  def handle(self):
    data = self.request.recv(200)
    incoming = data
    if not data:
      print "WARN: Broken reception."
      return

    client_ip = self.client_address[0]
    print "INFO: " + str(client_ip) + " connected!"
    for x in incoming:
        print x,
    app.label_7.setText(str(data))
    app.lineEdit_5.setText(str(data))


main()

