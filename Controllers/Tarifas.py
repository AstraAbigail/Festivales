import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos
from Database.conexion import conexion
from Models.Tarifas import Tarifas

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Tarifas_Control():
    
    def __init__(self, ventana):
        self.__tarifas_db = Tarifas(conexion())   
        self.__tarifas_ui = ventana


    def verificarCadenas(self):
        cadena = self.__tarifas_ui.lineEdit_tipoEntrada.text()        

        if  cadena.isalpha(): #caracteres del Alfabeto   
            self.buscarTarifa(cadena)
        else:     
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Verifique la informacion")
            msg.exec()            
          
         
    def verificarNumeros(self):
        cadena = self.__tarifas_ui.lineEdit_precio.text() 
        #print(cadena)
        num = ["0","1","2","3","4","5","6","7","8","9"]
        caracterEspecial = [".",","]  
        valido = False     
        valido_caracter = False  

        for x in cadena:
            if x in num:
                valido = True  
            elif x in caracterEspecial:         
                 valido_caracter = True
        if valido == True and valido_caracter == True:
            self.__tarifas_ui.pushButton_Tar_Ingresar.setEnabled(True)
               
        else:
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Verifique la informacion")
                msg.exec()

    def buscarTarifa(self,descripcion):
        resultado = self.__tarifas_db.searchTarifaByName(descripcion)
        self.__tarifas_ui.pushButton_Tar_Seleccionar.setEnabled(True) 
        self.showAll_Tarifas()
        if resultado != None:
            self.__tarifas_ui.lineEdit_tipoEntrada.clear()
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Esta Tarifa ya existe")
            msg.exec()

        

         
    def insertTarifa(self,descripcion,precio):        
        
        self.__tarifas_db.insertTarifa(descripcion,precio)                
       
        #refrescar la lista 
        self.showAll_Tarifas()
        #limpia el edit
        self.__tarifas_ui.lineEdit_tipoEntrada.clear() 
        self.__tarifas_ui.lineEdit_precio.clear() 
  
    def seleccionarTarifa(self):
        tabla_tarifas = self.__tarifas_ui.tableWidget_tarifas
        if tabla_tarifas.currentItem() !=None:   
            self.__tarifas_ui.pushButton_Tab_Eliminar.setEnabled(True)
            self.__tarifas_ui.pushButton_Tar_Editar.setEnabled(True)  
            
            descripcion = tabla_tarifas.currentItem().text()    
            global id_descripcion 
            id_descripcion = self.__tarifas_db.getIdTarifaSpecific(descripcion)  
            print("id_nombre seleccionado",id_descripcion[0])  

            tarifaSpecific = self.__tarifas_db.getTarifaSpecific(id_descripcion[0])  
            print(tarifaSpecific)          
            if tarifaSpecific: 
                self.__tarifas_ui.lineEdit_tipoEntrada.setText(str(tarifaSpecific[1]))
                self.__tarifas_ui.lineEdit_precio.setText(str(tarifaSpecific[2]))
     
    def modificarTarifa(self,descripcion,precio):       
            #tomo el id del seleccionar
            #print("id_descripcion del modificar", id_descripcion) #tupla
            #busco si el nombre que se ingreso, esta en la base de datos
            #tarifaSpecific = self.__tarifas_db.getTarifaSpecificbyName(id_descripcion[0])            
            #if str(tarifaSpecific[0]) != descripcion  and str(tarifaSpecific[1] != precio): #no hya  una categoria con ese nombre
                #si no existe la modifico               
                self.__tarifas_db.modificarTarifa(descripcion,precio,id_descripcion[0])
                #refrescar la lista 
                self.showAll_Tarifas()
                #limpia el edit
                self.__tarifas_ui.lineEdit_tipoEntrada.clear()
                self.__tarifas_ui.lineEdit_precio.clear()
          
                

    def eliminarTarifa(self):
        #print("is_nombre_eliminar",id_descripcion[0]) #cuando se selecciona el nombre de la tabla se saca el id  
        if id_descripcion[0] != None: #hay Id
            #si esta la borro
            self.__tarifas_db.eliminarTarifa(id_descripcion[0])
            #refrescar la lista 
            self.showAll_Tarifas()
        #limpia el edit            
        self.__tarifas_ui.lineEdit_categorias.clear()
        self.__tarifas_ui.lineEdit_precio.clear()

    def showAll_Tarifas(self):        
        tabla_tarifas = self.__tarifas_ui.tableWidget_tarifas
        categorias = self.__tarifas_db.getTarifas()   
        #print("showCategories:",categorias)
        tabla_tarifas.setRowCount(0)     
        if categorias:       
            self.__tarifas_ui.pushButton_Tar_Seleccionar.setEnabled(True)    
            for row, data in enumerate(categorias):                               
                    tabla_tarifas.insertRow(row)
                    for colum, data in enumerate(data):        
                        tabla_tarifas.setItem(row,colum,QtWidgets.QTableWidgetItem(str(data)))
    

