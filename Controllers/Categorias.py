import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos
from Database.conexion import conexion
from Models.Categorias import Categorias

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Categorias_Control():
    
    def __init__(self, ventana):
        self.__categorias_db = Categorias(conexion())   
        self.__categorias_ui = ventana


    


    def verificarCadenas(self):
        cadena = self.__categorias_ui.lineEdit_categorias.text()        

        if cadena.isalpha(): #caracteres del Alfabeto           
            self.__categorias_ui.pushButton_Cat_Ingresar.setEnabled(True)
            self.__categorias_ui.pushButton_Cat_Seleccionar.setEnabled(True)
            self.showAllCategorias()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Verifique la informacion")
            msg.exec()
         
    
    def insertCategoria(self,descripcion):
         #buscar que esa categoria no este ya agregada
        categoriaSpecific = self.__categorias_db.getCategoriaSpecific(descripcion)
        #print("categoria especifica",categoriaSpecific)
        if  categoriaSpecific == None:
            #print("entro al if")
            #si no existe la doy de alta
            self.__categorias_db.insertCategoria(descripcion)
            #refrescar la lista 
            self.showAllCategorias()
            #limpia el edit
            self.__categorias_ui.lineEdit_categorias.clear() 
        else:  
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Esta Categoria ya existe")
            msg.exec()   
            #refrescar la lista 
            self.showAllCategorias()
             #limpia el edit
            self.__categorias_ui.lineEdit_categorias.clear() 


    def selectCategoria(self):
        tabla_categoria = self.__categorias_ui.tableWidget_categorias
        if tabla_categoria.currentItem() !=None:   
            self.__categorias_ui.pushButton_Cat_Editar.setEnabled(True)
            self.__categorias_ui.pushButton_Cat_Eliminar.setEnabled(True)     
            nombre = tabla_categoria.currentItem().text()    
            global id_nombre 
            id_nombre = self.__categorias_db.getIdCategoriaSpecific(nombre)  
            #print("id_nombre seleccionado",id_nombre)  
            categoriaSpecific = self.__categorias_db.getCategoriaSpecific(nombre)            
            if categoriaSpecific: 
                self.__categorias_ui.lineEdit_categorias.setText(str(categoriaSpecific[1]))           
            


    def modificarCategoria(self,descripcion):       
            #tomo el id del seleccionar
            #print("id_nombre del modificar", id_nombre) #tupla
            #busco si el nombre que se ingreso, esta en la base de datos
            if descripcion == "":
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Campo vacio")
                msg.exec()    
            else:
                categoriaSpecific = self.__categorias_db.getCategoriaSpecific(descripcion)
                print(categoriaSpecific)
                if categoriaSpecific == None: #no hya  una categoria con ese nombre
                    #si no existe la modifico
                    self.__categorias_db.modificarCategoria(descripcion,id_nombre[0])
                    #refrescar la lista 
                    self.showAllCategorias()
                    #limpia el edit
                    self.__categorias_ui.lineEdit_categorias.clear() 
                else:  
                    msg = QMessageBox()
                    msg.setWindowTitle("Informacion")
                    msg.setText("")
                    msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                    msg.setInformativeText("La Categoria que quiere ingresar ya existe")
                    msg.exec()    
                    #limpia el edit
                    self.__categorias_ui.lineEdit_categorias.clear()
          

    def eliminarCategoria(self,descripcion):
        #print("is_nombre_eliminar",id_nombre) #cuando se selecciona el nombre de la tabla se saca el id      
        if id_nombre[0] != None: #hay Id
            #si esta la borro
            self.__categorias_db.eliminarCategoria(descripcion,id_nombre[0])
            #refrescar la lista 
            self.showAllCategorias()
            #limpia el edit
            self.__categorias_ui.lineEdit_categorias.clear()

    def showAllCategorias(self):        
        tabla_categoria = self.__categorias_ui.tableWidget_categorias
        categorias = self.__categorias_db.getCategorias()   
        #print("showCategories:",categorias)
        tabla_categoria.setRowCount(0)     
        if categorias:   
            self.__categorias_ui.pushButton_Cat_Seleccionar.setEnabled(True)        
            for row, data in enumerate(categorias):                               
                    tabla_categoria.insertRow(row)
                    for colum, data in enumerate(data):        
                        tabla_categoria.setItem(row,colum,QtWidgets.QTableWidgetItem(str(data)))
    

