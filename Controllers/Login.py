import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos
from Database.conexion import conexion
from Models.Usuarios import Usuarios
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox



class Login_control():

    def __init__(self, logIn):
        self.__usuarios_db = Usuarios(conexion())   
        self.__login_ui = logIn
     
        

    def verificarUsuario(self):
        usuario = self.__login_ui.lineEdit_usuario.text()        
        mayus = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        minus = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        User_valido_May = False
        User_valido_Min = False
        User_valido = False
        

        if len(usuario)<= 10  and len(usuario)>0 :         
            for x in usuario:
                if x in mayus:                                  
                    User_valido_May  = True
                if x in minus:                                      
                    User_valido_Min = True
            
            if User_valido_May and User_valido_Min:
                User_valido = True
                self.__login_ui.lineEdit_contrasena.setEnabled(True)
                return User_valido
            elif User_valido_May == False or User_valido_Min == False: 
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Verifique la informacion")
                msg.exec()
            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Ingrese nombre de Usuario")
            msg.exec() 

        
       
    
    def verificarContrasena(self):
        contrasena = self.__login_ui.lineEdit_contrasena.text()
        
        mayus = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        minus = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        num = ["0","1","2","3","4","5","6","7","8","9"]
        caracterEspecial = ["$","%","&","#","!","/","*","@","(",")","=","?","¡","¿","<",">"]
        
        Password_valido_May = False
        Password_valido_Min = False
        Password_valido_num = False
        Password_valido_carEsp = False
        Password_valido  = False
        

        if len(contrasena)<= 10  and len(contrasena)>0:            
            for x in contrasena:               
                if x in mayus:                    
                    Password_valido_May = True                            
                if x in minus:                    
                    Password_valido_Min  = True                           
                if x in num:                   
                    Password_valido_num = True                            
                if  x in caracterEspecial:                   
                    Password_valido_carEsp  = True

            
            if  Password_valido_May and  Password_valido_Min and Password_valido_num and Password_valido_carEsp:
                Password_valido = True
                self.__login_ui.pushButton_ingresar.setEnabled(True)
                return Password_valido
            
            elif Password_valido_May== False or  Password_valido_Min== False or Password_valido_num== False or Password_valido_carEsp== False: 
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Verifique la informacion")
                msg.exec()
                            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Ingrese contraseña")
            msg.exec() 

        

       
    def login(self,Ui_MainWindow,Ui_login):       

        b_U = self.verificarUsuario()
        b_C = self.verificarContrasena()
        
        
        
        if b_U==True and b_C == True:    
            Ui_login.hide()
            self.__login_ui.Form = QtWidgets.QMainWindow()
            self.__login_ui.ui = Ui_MainWindow()
            self.__login_ui.ui.setupUi(self.__login_ui.Form)
            self.__login_ui.Form.show()           
       









