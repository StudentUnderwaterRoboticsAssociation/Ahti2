import os
import interface
from PyQt4 import*
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import time
import threading
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



class App(QtGui.QMainWindow, interface.Ui_MainWindow):
	def __init__(self, parent = None):
		super(App, self).__init__(parent)
		self.setupUi(self)
		self.keepRunning = True
		self.serverState = False

	
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


		# t1 = threading.Thread(target = self.pushButton.clicked.connect(self.startServer))
		# t1.daemon = True
		# t1.start()
		self.pushButton.clicked.connect(self.startServer)
		self.pushButton_2.clicked.connect(self.shutServer)
		self.pushButton_7.clicked.connect(self.resetConnection)

	def resetConnection(self):
		
		print ("Server Restart Initiated")
		self.shutServer()
		time.sleep(2)
		self.startServer()

	def shutServer(self):
		self.keepRunning = False

		try:
			self.connection.close()
		except AttributeError:
			print "Trying to close a port which was never opened!"
		print "Disconnected"


	def core(self):
		while(1):
			self.connection, self.client_address = self.serverSocket.accept()
			try:
				print ("Connection from: ", self.client_address)
				data = self.connection.recv(500)
				if data:
					print data
					self.label_7.setText(str(data))
					self.textBrowser.setText(str(data))
			except:
				self.connection.close()


	def startServer(self):
		# IP = '10.78.18.2'
		# self.keepRunning = True
		# self.serverState = False
		# self.server = ThreadedTCPServer(('10.78.18.2',4242), requestHandler)
		# self.server_thread = threading.Thread(target = self.server.serve_forever)
		# self.server_thread.daemon = True
		# self.server_thread.start()
		# print "Server has started on :", IP
		# self.serverState = True
		# print "Shutdown"

		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = ('10.78.18.2', 4242)
		self.serverSocket.bind(server_address)
		self.serverSocket.listen(2)
		print ("Server started: ", server_address)
		#self.lineEdit_5.setText("Server started")
		self.connection, self.client_address = self.serverSocket.accept()
		try:
			print ("Connection from: ", self.client_address)
			self.lineEdit_5.setText("Connection from: " + str(self.client_address))
			data = self.connection.recv(500)
			if data:
				print data
				self.label_7.setText(str(data))
				self.lineEdit_5.setText(str(data))
		except:
			self.connection.close()

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



main()

