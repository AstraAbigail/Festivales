import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos
from Database.conexion import conexion
from Models.Eventos import Eventos
from Models.Estadios import Estadios
from Models.Categorias import Categorias
from Models.Tickets import Tickets

from datetime import datetime,timedelta,time
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
MAYUS = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NUM = ["0","1","2","3","4","5","6","7","8","9",]
class Evento_Control():
    
    def __init__(self, crearEvento):
        self.__evento_db = Eventos(conexion())   
        self.__evento_ui = crearEvento
        self.__estadios = Estadios(conexion())
        self.__categorias = Categorias(conexion())
        self.__tickets = Tickets(conexion())


    def showWindowEvento(self,pantallaMostrar):
         #pasar a la otra pantalla
            #Ui_login.hide()
            self.__evento_ui.Form = QtWidgets.QMainWindow()
            self.__evento_ui.ui = pantallaMostrar()
            self.__evento_ui.ui.setupUi(self.__evento_ui.Form)
            self.__evento_ui.Form.show()  

    def verificarCadenas(self):             
        valido=False
        valido_num = False  
        cadena = self.__evento_ui.lineEdit_nombre.text() 
        print(cadena)       
        for x in cadena:
            if x in MAYUS: 
              valido = True
            elif x in NUM: 
                valido_num = True  
              
        if valido == True or valido_num == True:
            print("entroooo 2")   
            ya_ingresado = self.__evento_db.showEventsByName(cadena) 
            print(ya_ingresado) 
            if ya_ingresado == []:
                print("entroooo 3")   
                self.__evento_ui.dateEdit_inicio.setEnabled(True)
                self.__evento_ui.dateEdit_fin.setEnabled(True)
                self.__evento_ui.timeEdit_inicio.setEnabled(True)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Evento ya ingresado")
                self.__evento_ui.lineEdit_nombre.clear()
                msg.exec() 
            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Ingrese solamente letras y numeros")
            self.__evento_ui.lineEdit_nombre.clear()
            msg.exec() 


    def verificarInt(self):
        cadena = self.__evento_ui.lineEdit_ano.text()        
        if cadena.isdigit():  #numeros
             return True
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("Formato requerido: YYYY")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Ingrese solamente numeros")
            self.__evento_ui.lineEdit_nombre.clear()
            msg.exec() 
    
    
    def inicializar_comboBoxEstadios(self):             
        infoCombo = self.__estadios.cargarComboEstadios()         
        for item in infoCombo:
            for x in item:                              
                self.__evento_ui.comboBox_estadios.addItem(x)
    def inicializar_comboBoxCategorias(self):
        infoCombo = self.__categorias.cargarComboCategorias()         
        for item in infoCombo:
            for x in item:                              
                self.__evento_ui.comboBox_categoria.addItem(x)

    def cargar(self,nombre,lugar,categoria,fechainicio,fechafin,horainicio):        
        #chequear que no este ya cargado o no haya algun festival con mismo nombre y ubicacion
        ya_ingresado = self.__evento_db.showEventsByName(nombre)
        #print(ya_ingresado) #[(),(),()]

        if ya_ingresado == []: #hay un evento con ese nombre          
            eliminado = "No"
            self.__evento_db.cargar(nombre,lugar,categoria,fechainicio,fechafin,horainicio,eliminado)
            self.__evento_ui.lineEdit_nombre.clear()
            self.mostrarEventos()

            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Evento dado de Alta")        
            msg.exec()         
            
        else: 
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("El evento ya esta en la Base de Datos")        
            msg.exec()         
            self.mostrarEventos()
            
    
    def mostrarEventos(self):        
        tabla_eventos = self.__evento_ui.tableWidget_crearEvento
        eventos = self.__evento_db.getEvents()   
        
        tabla_eventos.setRowCount(0)     
        if eventos: 
            self.__evento_ui.pushButton_seleccionar.setEnabled(True)
            self.__evento_ui.dateEdit_inicio.setEnabled(True)
            self.__evento_ui.dateEdit_fin.setEnabled(True)
            self.__evento_ui.timeEdit_inicio.setEnabled(True)          
            for row, data in enumerate(eventos):                               
                    tabla_eventos.insertRow(row)
                    for colum, data in enumerate(data):        
                        tabla_eventos.setItem(row,colum,QtWidgets.QTableWidgetItem(str(data))) 
    
    def seleccionar(self):        
        tabla_eventos = self.__evento_ui.tableWidget_crearEvento
        if tabla_eventos.currentItem() != None:   

            self.__evento_ui.pushButton_eliminar.setEnabled(True)
            self.__evento_ui.pushButton_modificar.setEnabled(True)  
            
            descripcion = tabla_eventos.currentItem().text()    
            print(descripcion)                 

            global id_descripcion
            id_descripcion = self.__evento_db.getIdEventoSpecific(descripcion)  
            print("id_nombre seleccionado",id_descripcion) #anda 1           

            if id_descripcion != None:  #presiono el nombre
                eventoSpecific = self.__evento_db.getEventoSpecificById(id_descripcion) 
                print(eventoSpecific)  
                #la hora no la trae por problemas de tipo
                if eventoSpecific: 
                    for x in eventoSpecific:
                        self.__evento_ui.lineEdit_nombre.setText(str(x[0]))
                        self.__evento_ui.comboBox_estadios.setCurrentText(x[1])
                        self.__evento_ui.comboBox_categoria.setCurrentText(x[2])
                        self.__evento_ui.dateEdit_inicio.setDate(x[3])                         
                        self.__evento_ui.dateEdit_fin.setDate(x[4])                                  
                        break
                    
    def tieneTickets(self,nombre,lugar):
        id_lugar = self.__estadios.searchIdByName(lugar) 
        id_evento = self.__evento_db.getIdEventoSpecific(nombre)
        #print(id_lugar[0])
        #print(id_evento)
        return self.__tickets.tieneTickets(id_evento,id_lugar[0])
    
    
    def modificar(self,nombre,lugar,categoria,fechaIni,hora,fechaFin):
        tickets_vendidos = self.tieneTickets(nombre,lugar)
        #print("Tickets: ",tickets_vendidos)
        if tickets_vendidos != []: 
            #hay un ticket vendido para ese evento, en ese lugar 
            #no se puede modificar
            msg = QMessageBox()
            msg.setWindowTitle("Advertencia")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Critical) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("El evento posee tickets vendido, no se puede modificar")        
            msg.exec() 
        else:
            #print("entro al modificar")
            self.__evento_db.modificar(nombre,lugar,categoria,fechaIni,hora,fechaFin,id_descripcion)           
            self.__evento_ui.lineEdit_nombre.clear()
            self.mostrarEventos()
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Evento modificado")        
            msg.exec() 
    
    def eliminar(self,nombre,lugar):
        eliminado = "Si"
        tickets_vendidos = self.tieneTickets(nombre,lugar)
        if tickets_vendidos != []: 
            msg = QMessageBox()
            msg.setWindowTitle("Advertencia")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Critical) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("El evento posee tickets vendido, no se puede eliminar")        
            msg.exec() 
        else:    
            self.__evento_db.eliminar(eliminado,id_descripcion)
            self.mostrarEventos()
            self.__evento_ui.lineEdit_nombre.clear()
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Evento Eliminado")        
            msg.exec() 
        