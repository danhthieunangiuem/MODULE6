# Form implementation generated from reading ui file 'C:\Users\ACER\PycharmProjects\MODULE 8\Ex134\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 512)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 10, 641, 181))
        self.widget.setStyleSheet("\n"
"background-color: rgb(165, 165, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_name = QtWidgets.QLabel(parent=self.widget)
        self.label_name.setGeometry(QtCore.QRect(30, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_email = QtWidgets.QLabel(parent=self.widget)
        self.label_email.setGeometry(QtCore.QRect(30, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.label_gender = QtWidgets.QLabel(parent=self.widget)
        self.label_gender.setGeometry(QtCore.QRect(30, 130, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_gender.setFont(font)
        self.label_gender.setObjectName("label_gender")
        self.radioButton_man = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_man.setGeometry(QtCore.QRect(210, 130, 95, 20))
        self.radioButton_man.setObjectName("radioButton_man")
        self.radioButton_woman = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_woman.setGeometry(QtCore.QRect(390, 130, 95, 20))
        self.radioButton_woman.setObjectName("radioButton_woman")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_name.setGeometry(QtCore.QRect(170, 40, 441, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_email = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_email.setGeometry(QtCore.QRect(170, 90, 441, 31))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(80, 220, 641, 181))
        self.widget_2.setStyleSheet("background-color: rgb(255, 110, 97);")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(430, 0, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_address = QtWidgets.QLabel(parent=self.widget_2)
        self.label_address.setGeometry(QtCore.QRect(30, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_address.setFont(font)
        self.label_address.setObjectName("label_address")
        self.label_education = QtWidgets.QLabel(parent=self.widget_2)
        self.label_education.setGeometry(QtCore.QRect(30, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_education.setFont(font)
        self.label_education.setObjectName("label_education")
        self.radioButton_bachelor = QtWidgets.QRadioButton(parent=self.widget_2)
        self.radioButton_bachelor.setGeometry(QtCore.QRect(170, 90, 95, 20))
        self.radioButton_bachelor.setObjectName("radioButton_bachelor")
        self.radioButton_master = QtWidgets.QRadioButton(parent=self.widget_2)
        self.radioButton_master.setGeometry(QtCore.QRect(320, 90, 95, 20))
        self.radioButton_master.setObjectName("radioButton_master")
        self.lineEdit_address = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_address.setGeometry(QtCore.QRect(170, 40, 441, 31))
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.radioButton_doctoral = QtWidgets.QRadioButton(parent=self.widget_2)
        self.radioButton_doctoral.setGeometry(QtCore.QRect(460, 90, 95, 20))
        self.radioButton_doctoral.setObjectName("radioButton_doctoral")
        self.pushButtonSendData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSendData.setGeometry(QtCore.QRect(350, 420, 101, 41))
        self.pushButtonSendData.setObjectName("pushButtonSendData")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "Personal Information:"))
        self.label_name.setText(_translate("MainWindow", "Full Name:"))
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.label_gender.setText(_translate("MainWindow", "Gender:"))
        self.radioButton_man.setText(_translate("MainWindow", "Man"))
        self.radioButton_woman.setText(_translate("MainWindow", "Woman"))
        self.label_5.setText(_translate("MainWindow", "Other Information:"))
        self.label_address.setText(_translate("MainWindow", "Address:"))
        self.label_education.setText(_translate("MainWindow", "Education:"))
        self.radioButton_bachelor.setText(_translate("MainWindow", "Bachelor"))
        self.radioButton_master.setText(_translate("MainWindow", "Master"))
        self.radioButton_doctoral.setText(_translate("MainWindow", "Doctoral"))
        self.pushButtonSendData.setText(_translate("MainWindow", "Send Data"))
