# Form implementation generated from reading ui file 'C:\Users\ACER\PycharmProjects\MODULE 8\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 255, 255);\n"
"font: 25 14pt \"Poppins Light\";")
        self.label.setObjectName("label")
        self.label_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(50, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_email = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(50, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(190, 70, 361, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(190, 120, 361, 31))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 160, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(85, 255, 255);\n"
"font: 25 13pt \"Poppins Light\";\n"
"background-color: rgb(246, 255, 60);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.checkBox_ml = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_ml.setGeometry(QtCore.QRect(190, 220, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_ml.setFont(font)
        self.checkBox_ml.setObjectName("checkBox_ml")
        self.checkBox_dl = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_dl.setGeometry(QtCore.QRect(190, 270, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_dl.setFont(font)
        self.checkBox_dl.setObjectName("checkBox_dl")
        self.checkBox_sc = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_sc.setGeometry(QtCore.QRect(190, 320, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_sc.setFont(font)
        self.checkBox_sc.setObjectName("checkBox_sc")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 380, 111, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
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
        self.label.setText(_translate("MainWindow", "Courses Registration"))
        self.label_name.setText(_translate("MainWindow", "Full Name:"))
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.label_4.setText(_translate("MainWindow", "Courses Selection:"))
        self.checkBox_ml.setText(_translate("MainWindow", "Machine Learning"))
        self.checkBox_dl.setText(_translate("MainWindow", "Deep Learning"))
        self.checkBox_sc.setText(_translate("MainWindow", "Smart Contact"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
