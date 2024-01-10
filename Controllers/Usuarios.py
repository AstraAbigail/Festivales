import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos
from Database.conexion import conexion
from Models.Usuarios import Usuarios

class Usuarios_Control():

    def __init__(self, Users):
        self.usuarios_db = Usuarios(conexion())   
        self.usuarios_ui = Users


    