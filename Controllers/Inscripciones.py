import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos
from Database.conexion import conexion
from Models.Inscripciones import Inscrpciones
from Models.Categorias import Categorias
from Models.Tickets   import Tickets

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
MAYUS = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NUM = ["0","1","2","3","4","5","6","7","8","9"]
ESPECIAL = [".","_","@","-"]  

class Inscripciones_Control():
    
    def __init__(self, inscripciones):
        self.__inscripciones_db = Inscrpciones(conexion())   
        self.__inscripciones_ui = inscripciones
        self.__categorias_db = Categorias(conexion())
        self.__tickets_bd = Tickets(conexion())

    def showWindowInscripciones(self,pantallaMostrar):
         #pasar a la otra pantalla        
            self.__inscripciones_ui.Form = QtWidgets.QMainWindow()
            self.__inscripciones_ui.ui = pantallaMostrar()
            self.__inscripciones_ui.ui.setupUi(self.__inscripciones_ui.Form)
            self.__inscripciones_ui.Form.show()  

    def verificarCadenas(self):
        cadena = self.__inscripciones_ui.lineEdit_nombre.text()
        categoria = self.__inscripciones_ui.comboBox_categoria.currentText()
        valido = False
        for x in cadena:
            if x in MAYUS:
                valido = True
        if valido == True:
            ya_ingresado = self.__inscripciones_db.showId_InscripcionesByNombreCategoria(cadena,categoria)
            print(ya_ingresado)
            if ya_ingresado == [] or ya_ingresado == None:
                #habilito edits Correo
                self.__inscripciones_ui.lineEdit_correo.setEnabled(True)
                self.__inscripciones_ui.lineEdit_correo.setFocus()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Warning) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("La inscripcion ya se encuentra en la base de datos")
                self.__inscripciones_ui.lineEdit_nombre.clear()
                msg.exec() 
        else:
            self.__inscripciones_ui.lineEdit_nombre.clear()
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Warning) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Ingrese solamente letras")
            self.__inscripciones_ui.lineEdit_correo.clear()
            msg.exec() 

    def verificarNumCaracter(self):
        cadena =  self.__inscripciones_ui.lineEdit_correo.text()
        valido_num = False
        valido_caracter = False
        valido_letras = False
        
        for x in cadena:
            if x in NUM:
                valido_num = True
        for y in cadena:
            if y in ESPECIAL:
                valido_caracter = True
        for z in cadena:
            if z in MAYUS:
                valido_letras = True
        
        if valido_num == True or valido_caracter == True and valido_letras == True:
            #habilito edits detalle
            self.__inscripciones_ui.lineEdit_detalle.setEnabled(True)
            self.__inscripciones_ui.lineEdit_detalle.setFocus()

            self.__inscripciones_ui.pushButton_cargar.setEnabled(True)
            self.__inscripciones_ui.pushButton_seleccionar.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Ingrese, numeros, letras y/o .  ,  @ -  _")
            self.__inscripciones_ui.lineEdit_correo.clear()
            msg.exec() 

    def inicializar_comboBoxCategorias(self):
        infoCombo = self.__categorias_db.cargarComboCategorias()         
        for item in infoCombo:
            for x in item:                              
                self.__inscripciones_ui.comboBox_categoria.addItem(x) 
    
   
    def cargar(self,categoria,nombre,detalle,correo):
        #chequear que no este ya cargado o no haya algun festival con mismo nombre y ubicacion
        ya_ingresado = self.__inscripciones_db.showId_InscripcionesByNombreCategoria(nombre,categoria)

        if ya_ingresado != None:
            self. mostrarInscriptos()   
            self.__inscripciones_ui.lineEdit_nombre.clear()
            self.__inscripciones_ui.lineEdit_correo.clear()
            self.__inscripciones_ui.lineEdit_detalle.clear()   
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("La Inscripcion ya se encuentra en nuestros datos.")        
            msg.exec() 
            #ya se ingreso
        else:
            eliminado = "No"
            if detalle == "":
                detalle = ""
            self.__inscripciones_db.cargar(categoria,nombre,detalle,correo,eliminado)
            self.__inscripciones_ui.lineEdit_nombre.clear()
            self.__inscripciones_ui.lineEdit_correo.clear()
            self.__inscripciones_ui.lineEdit_detalle.clear()            
            self. mostrarInscriptos()    

            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Inscripcion completada")        
            msg.exec() 

    def  mostrarInscriptos(self):        
        tabla_inscriptos = self.__inscripciones_ui.tableWidget_inscripciones
        eventos = self.__inscripciones_db.getInscriptos() 
        tabla_inscriptos.setRowCount(0)     
        if eventos:  
            self.__inscripciones_ui.pushButton_seleccionar.setEnabled(True)         
            for row, data in enumerate(eventos):                               
                    tabla_inscriptos.insertRow(row)
                    for colum, data in enumerate(data):        
                        tabla_inscriptos.setItem(row,colum,QtWidgets.QTableWidgetItem(str(data))) 
    
    def seleccionar(self): 
        tabla_inscripciones = self.__inscripciones_ui.tableWidget_inscripciones
        if tabla_inscripciones.currentItem() != None:   

            self.__inscripciones_ui.pushButton_eliminar.setEnabled(True)
            self.__inscripciones_ui.pushButton_modificar.setEnabled(True)  
            
            descripcion = tabla_inscripciones.currentItem().text()    
            #print(descripcion)                 

            global id_inscripcion
            id_inscripcion = self.__inscripciones_db.getIdInscripcionSpecific(descripcion)  
            #print("id: ",id_inscripcion) #anda 1           

            if id_inscripcion != None:  #presiono el nombre
                specific = self.__inscripciones_db.getInscripcionSpecificById(id_inscripcion) 
                #print(specific)  

                if specific: 
                    for x in specific:                      
                        self.__inscripciones_ui.lineEdit_nombre.setText(str(x[0]))
                        self.__inscripciones_ui.lineEdit_correo.setText(str(x[1]))
                        self.__inscripciones_ui.lineEdit_detalle.setText(str(x[2]))   
                        self.__inscripciones_ui.comboBox_categoria.setCurrentText(x[3])

    def modificar(self,categoria,nombre,detalle,correo):
        id_nombre = self.__inscripciones_db.getIdByName(nombre)
        #print(id_nombre[0])
        tickets = self.__tickets_bd.ticketsInscripcion(id_nombre[0])
        
        if tickets != None: #no se pued emodificar es para cuando no hay nada cargado
            msg = QMessageBox()
            msg.setWindowTitle("Advertencia")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Critical) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("La Inscripcion posee tickets vendido, no se puede modificar")        
            msg.exec() 
        else:
            self.__inscripciones_db.modificar(categoria,nombre,detalle,correo,id_inscripcion)           
            self.__inscripciones_ui.lineEdit_nombre.clear()
            self.__inscripciones_ui.lineEdit_correo.clear()
            self.__inscripciones_ui.lineEdit_detalle.clear()            
            self. mostrarInscriptos()    
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Inscripcion modificada")        
            msg.exec()      

    def eliminar(self,nombre):
        id_nombre = self.__inscripciones_db.getIdByName(nombre)
        tickets = self.__tickets_bd.ticketsInscripcion(id_nombre[0])
        
        if tickets != None:#no se puede eliminar
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Inscripcion con tickets en venta, no se puede eliminar")        
            msg.exec()
        else:
            eliminado = "Si"
            self.__inscripciones_db.eliminar(eliminado,id_inscripcion)
            self.mostrarInscriptos()
            self.__inscripciones_ui.lineEdit_nombre.clear()
            self.__inscripciones_ui.lineEdit_correo.clear()
            self.__inscripciones_ui.lineEdit_detalle.clear()  
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Inscripcion Eliminada")        
            msg.exec()
                  