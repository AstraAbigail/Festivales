import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QEvent
from Controllers.Login import Login_control
from Views.menu_principal_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def __init__(self):
                self.login_controlles = Login_control(self)
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(400, 300)
        login.setMinimumSize(QtCore.QSize(400, 300))
        login.setMaximumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        login.setFont(font)
        login.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        login.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        login.setStyleSheet("background-color: rgb(203, 203, 151);")
        self.pushButton_ingresar = QtWidgets.QPushButton(parent=login)
        self.pushButton_ingresar.setGeometry(QtCore.QRect(140, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_ingresar.setFont(font)
        self.pushButton_ingresar.setStyleSheet("\n"
"background-color: rgb(0, 51, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);")
        self.pushButton_ingresar.setObjectName("pushButton_ingresar")
        self.label = QtWidgets.QLabel(parent=login)
        self.label.setGeometry(QtCore.QRect(150, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=login)
        self.label_3.setGeometry(QtCore.QRect(130, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_contrasena = QtWidgets.QLineEdit(parent=login)
        self.lineEdit_contrasena.setGeometry(QtCore.QRect(90, 170, 211, 41))
        self.lineEdit_contrasena.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.lineEdit_contrasena.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"")
        self.lineEdit_contrasena.setMaxLength(10)
        self.lineEdit_contrasena.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_contrasena.setObjectName("lineEdit_contrasena")
        self.lineEdit_usuario = QtWidgets.QLineEdit(parent=login)
        self.lineEdit_usuario.setGeometry(QtCore.QRect(90, 90, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_usuario.setFont(font)
        self.lineEdit_usuario.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.lineEdit_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"")
        self.lineEdit_usuario.setMaxLength(10)
        self.lineEdit_usuario.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)


  #----------------------------------------------------
        self.lineEdit_contrasena.setEnabled(False)
        self.pushButton_ingresar.setEnabled(False)

        #verificar Edits - tocando el enter     

        self.lineEdit_usuario.returnPressed.connect(self.login_controlles.verificarUsuario)
        self.lineEdit_contrasena.returnPressed.connect(self.login_controlles.verificarContrasena) 
        
        #botones
        self.ingresar = self.pushButton_ingresar.clicked.connect(lambda:self.login_controlles.login(Ui_MainWindow,login))
        
        
       
        #------------------------------------------------------------


        login.setTabOrder(self.lineEdit_usuario, self.lineEdit_contrasena)
        login.setTabOrder(self.lineEdit_contrasena, self.pushButton_ingresar)



    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Inicio Sesion"))
        self.pushButton_ingresar.setText(_translate("login", "INGRESAR"))
        self.label.setText(_translate("login", "USUARIO"))
        self.label_3.setText(_translate("login", "CONTRASEÑA"))

if __name__ == "__main__":
                import sys
                app = QtWidgets.QApplication(sys.argv)
                LogIn = QtWidgets.QMainWindow()
                ui = Ui_login()
                ui.setupUi(LogIn)      
                LogIn.show()
                sys.exit(app.exec())