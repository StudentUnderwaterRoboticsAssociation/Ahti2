# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1205, 828)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 1171, 731))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 250, 691, 141))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 50, 141, 51))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalSlider_4 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(290, 49, 261, 51))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(50, 410, 691, 121))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalSlider_3 = QtGui.QSlider(self.groupBox_4)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(110, 40, 491, 51))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(80, 56, 31, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(760, 0, 371, 661))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.progressBar = QtGui.QProgressBar(self.groupBox_3)
        self.progressBar.setGeometry(QtCore.QRect(30, 70, 321, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar_2 = QtGui.QProgressBar(self.groupBox_3)
        self.progressBar_2.setGeometry(QtCore.QRect(30, 137, 321, 31))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.progressBar_3 = QtGui.QProgressBar(self.groupBox_3)
        self.progressBar_3.setGeometry(QtCore.QRect(30, 200, 321, 31))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(164, 50, 66, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(171, 120, 66, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(169, 183, 66, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.progressBar_4 = QtGui.QProgressBar(self.groupBox_3)
        self.progressBar_4.setGeometry(QtCore.QRect(30, 260, 321, 31))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName(_fromUtf8("progressBar_4"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(152, 240, 101, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(50, 0, 681, 241))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalSlider = QtGui.QSlider(self.groupBox)
        self.horizontalSlider.setGeometry(QtCore.QRect(100, 35, 491, 51))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider_2 = QtGui.QSlider(self.groupBox)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(100, 80, 491, 51))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 55, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(11, 105, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(140, 190, 71, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 155, 141, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 155, 141, 51))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(50, 560, 321, 111))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.pushButton_15 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_15.setGeometry(QtCore.QRect(90, 40, 141, 51))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(410, 560, 321, 111))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.pushButton_16 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_16.setGeometry(QtCore.QRect(90, 40, 141, 51))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(40, 20, 321, 361))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit.setGeometry(QtCore.QRect(30, 34, 181, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 34, 51, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(90, 68, 71, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(240, 68, 31, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(30, 98, 121, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 98, 121, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 160, 121, 41))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 160, 121, 41))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 220, 181, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 214, 81, 41))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(33, 270, 71, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(120, 270, 71, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 300, 101, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_10.setGeometry(QtCore.QRect(160, 290, 141, 41))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(383, 17, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(380, 50, 731, 71))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1205, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Led", None))
        self.pushButton_5.setText(_translate("MainWindow", "Led", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Camera", None))
        self.label_11.setText(_translate("MainWindow", "0", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Processes", None))
        self.label_8.setText(_translate("MainWindow", "Gripper", None))
        self.label_9.setText(_translate("MainWindow", "Wrist", None))
        self.label_10.setText(_translate("MainWindow", "Camera", None))
        self.label_12.setText(_translate("MainWindow", "Light Intensity", None))
        self.groupBox.setTitle(_translate("MainWindow", "Gripper Controls", None))
        self.label.setText(_translate("MainWindow", "Gripper", None))
        self.label_2.setText(_translate("MainWindow", "Wrist", None))
        self.label_3.setText(_translate("MainWindow", "Clockwise", None))
        self.pushButton_3.setText(_translate("MainWindow", "Counter clockwise", None))
        self.pushButton_4.setText(_translate("MainWindow", "Clockwise", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Inflation System Control", None))
        self.pushButton_15.setText(_translate("MainWindow", "Gripper", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Graph", None))
        self.pushButton_16.setText(_translate("MainWindow", "Graph", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Rover Network", None))
        self.label_4.setText(_translate("MainWindow", "IP Address", None))
        self.label_5.setText(_translate("MainWindow", "Port", None))
        self.pushButton.setText(_translate("MainWindow", "Connect", None))
        self.pushButton_2.setText(_translate("MainWindow", "Disconnect", None))
        self.pushButton_7.setText(_translate("MainWindow", "Reset", None))
        self.pushButton_8.setText(_translate("MainWindow", "Ping", None))
        self.pushButton_9.setText(_translate("MainWindow", "Send", None))
        self.label_6.setText(_translate("MainWindow", "Received:", None))
        self.label_7.setText(_translate("MainWindow", "nill", None))
        self.pushButton_10.setText(_translate("MainWindow", "Refresh Rate", None))
        self.label_13.setText(_translate("MainWindow", "Network terminal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))

