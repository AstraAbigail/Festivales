import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos

from Views.main_configuracion_ui import Ui_MainWindow_configuracion

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

class MenuPrincipal_Control():
    
    def __init__(self, ventana):          
        self.__menuprincipal_ui = ventana


    def showWindowConfiguracion(self,pantallaMostrar):
         #pasar a la otra pantalla
            #Ui_login.hide()
            self.__menuprincipal_ui.Form = QtWidgets.QMainWindow()
            self.__menuprincipal_ui.ui = pantallaMostrar()
            self.__menuprincipal_ui.ui.setupUi(self.__menuprincipal_ui.Form)
            self.__menuprincipal_ui.Form.show() 