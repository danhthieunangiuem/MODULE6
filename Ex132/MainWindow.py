# Form implementation generated from reading ui file 'C:\Users\ACER\PycharmProjects\MODULE 8\Ex132\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 90, 400, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\ACER\\PycharmProjects\\MODULE 8\\Ex132\\images/image1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.checkBox_showhide = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_showhide.setGeometry(QtCore.QRect(130, 30, 391, 31))
        self.checkBox_showhide.setObjectName("checkBox_showhide")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_showhide.setText(_translate("MainWindow", "Show/Hide Image"))
