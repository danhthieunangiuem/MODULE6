# Form implementation generated from reading ui file 'C:\Users\ACER\PycharmProjects\HelloWorld\MyQMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 245)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSendName = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSendName.setGeometry(QtCore.QRect(40, 130, 151, 41))
        self.pushButtonSendName.setObjectName("pushButtonSendName")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(40, 70, 491, 31))
        self.lineEditName.setObjectName("lineEditName")
        self.pushButtonVisitBlog = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonVisitBlog.setGeometry(QtCore.QRect(210, 130, 151, 41))
        self.pushButtonVisitBlog.setObjectName("pushButtonVisitBlog")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(380, 130, 151, 41))
        self.pushButtonExit.setObjectName("pushButtonExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Le Hoai Thanh Danh - QMainWindow"))
        self.pushButtonSendName.setText(_translate("MainWindow", "Send Name"))
        self.label.setText(_translate("MainWindow", "Your Name:"))
        self.lineEditName.setText(_translate("MainWindow", "Le Hoai Thanh Danh"))
        self.pushButtonVisitBlog.setText(_translate("MainWindow", "Visit Blog"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
