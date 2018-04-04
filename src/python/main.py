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
    os.system("clear")
    os.system("pip install qdarkstyle")
    os.system("python main.py")
import sys
os.system("pyuic4 -o interface.py interface.ui")


class App(QtGui.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, parent = None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.keepRunning     = True
        self.serverState     = False
        self.universalLock   = False
        self.commandList     = []
    
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

        self.lineEdit.setText('192.168.2.133')
        self.lineEdit_2.setText('4242')
       

        self.pushButton.clicked.connect(self.startServer)
        self.pushButton_2.clicked.connect(self.shutConnection)
        self.pushButton_7.clicked.connect(self.resetConnection)
        self.pushButton_9.clicked.connect(self.sendData)

        #Universal LOCk LOOP  
        t2 = threading.Thread(target = self.backgroundRun)
        t2.daemon = True
        t2.start()


    def sendData(self):
        self.serverConnect(self.lineEdit_3.text())

    def backgroundRun(self):
        while(1):
            if self.universalLock != True:
                self.tab.setEnabled(False)
            elif self.universalLock:
                self.tab.setEnabled(True)

    def serverConnect(self, dataPacket):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address = (str(self.lineEdit.text()), 4242)
        sock.connect(server_address)
        sock.sendall(str(dataPacket))
        data = sock.recv(100)
        print data
        sock.close()

    def resetConnection(self):
        print ("Server Restart Initiated")
        self.universalLock = False
        #self.t1.join()
        time.sleep(2)
        self.startServer()

    def shutConnection(self):
        self.universalLock = False

    def core(self):
        self.serverConnect("Initiation Command")
            
    def startServer(self):
        self.universalLock = True
        self.t1 = threading.Thread(target = self.core)
        self.t1.daemon = True
        self.t1.start()
        
    def rotateClockwise(self):
        self.serverConnect("Rotate ClockWise")
    
    def rotateAntiClockwise(self):
        self.serverConnect("Rotate rotateAntiClockwise")

    def openGripper(self, x):
        self.progressBar.setValue(x)
        self.serverConnect(x)

    def rotateGripper(self,x):
        self.progressBar_2.setValue(x)
        self.serverConnect(x)

    def panCamera(self, x):
        self.progressBar_3.setValue(x)
        self.serverConnect(x)

    def ledsBrightness(self, x):
        self.progressBar_4.setValue(x)
        self.serverConnect(x)

    def inflationGripper(self):
        if self.pushButton_15.isChecked():
            print "Open"
            self.pushButton_15.setText("Open")
            self.serverConnect("Inflation Gripper Open")
        else:
            print "Close"
            self.pushButton_15.setText("Close")
            self.serverConnect("Inflation Gripper Close")
    
    def ledControl(self):
        if self.pushButton_5.isChecked():
            print "Off"
            self.horizontalSlider_4.setEnabled(False)
            self.pushButton_5.setText("Off")   
            self.serverConnect("Led Off")
        else:
            print "On"
            self.horizontalSlider_4.setEnabled(True)
            self.pushButton_5.setText("On")

            self.serverConnect("Led On")

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
    form = App()
    form.run()
    form.show()
    app.exec_()

main()

