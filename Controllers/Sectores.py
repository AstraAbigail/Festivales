import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos
from Database.conexion import conexion
from Models.Sectores import Sectores
from Models.Tickets import Tickets
from Models.Estadios import Estadios 

#from Controllers.Estadios import Estadio_Control

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox


MAYUS = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CARACTER_ESPECIAL = ["$","%","&","#"," ","!","/","*",",",".","@","(",")","=","?","¡","¿","<",">"]
NUM =   ["0","1","2","3","4","5","6","7","8","9"]
global inicio,fin
FILAS = 20
inicio=0
fin = 0

class Sector_Control():
    
    def __init__(self, ventana):
        self.__sectores_db = Sectores(conexion())   
        self.__sectores_ui = ventana
        self.__tickets_bd = Tickets(conexion())
        self.__estadios_bd = Estadios(conexion())
       

    def validarNombre(self):
        existeNombre = False
        cadena = self.__sectores_ui.lineEdit_nombreSector.text()
        valido=False
        id_estadio = self.__sectores_db.searchIdEstadiobyName(self.__sectores_ui.lineEdit_nombre.text()) 
        id_ = id_estadio[0]
        BD_nombre = self.__sectores_db.SearchNameSectorByName(id_)        
        for x in BD_nombre:           
            if str(x[0]) == cadena:
                existeNombre = True
                break

        if existeNombre == True:   
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Elija otro nombre")
                msg.exec() 
        else:
            for x in cadena:
                if x in MAYUS:
                    valido = True
            if valido:
                
                #habilito colores
                self.__sectores_ui.lineEdit_color.setEnabled(True)
                self.__sectores_ui.lineEdit_color.setFocus()
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Boton Colores habilitado")
                msg.exec() 

    def validarColor(self):
        existeColor = False
        cadena = self.__sectores_ui.lineEdit_color.text()
        valido=False
        contador = 0
        id_estadio = self.__sectores_db.searchIdEstadiobyName(self.__sectores_ui.lineEdit_nombre.text()) 
        id_ = id_estadio[0]
        BD_color = self.__sectores_db.SearchColorSectorByName(id_)       
        for x in BD_color:
            if str(x[0]) == cadena:
                existeColor = True

        if existeColor == True:  
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Elija otro color")
            msg.exec() 
        else:
            for x in cadena:
                if x in MAYUS:
                    contador += 1
                    valido = True
            
            if valido and contador == len(cadena):
                #habilito precio
                self.__sectores_ui.lineEdit_precioSector.setEnabled(True)
                self.__sectores_ui.lineEdit_precioSector.setFocus()
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Boton Precio habilitado")
                msg.exec() 
        
    def validarPrecio(self):
        cadena = self.__sectores_ui.lineEdit_precioSector.text()
        valido=False
        contador = 0
        for x in cadena:
            if x in NUM:
                contador +=1
                valido = True

        if valido and contador == len(cadena):
            
            #Activar Boton Ingresar Sector y Seleccionar Sector
            self.__sectores_ui.pushButton_Est_Ingresar.setEnabled(True)
            self.__sectores_ui.pushButton_Est_Seleccionar.setEnabled(True)
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Botones  habilitados ")
            msg.exec()  


    def verificarNumeros(self):
        cadena = self.__sectores_ui.lineEdit_cantSectores.text()

        if cadena.isdigit():
            self.__sectores_ui.pushButton_verificar.setEnabled(True)   
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Dato Correcto")
            msg.exec()       
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Solamente numeros")
            msg.exec() 
    
    def verificar(self,cantidadTotal,cantidadSector):      
        v_capTotal = False
        v_canSectores = False



        if cantidadTotal == " ":            
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Busque Estadio primero, se necesita CAP.TOTAL")
            msg.exec() 
        else:
            v_capTotal = True

        if cantidadSector == " ":            
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Ingrese Cant. sectores")
            msg.exec()
        else:           
            v_canSectores  = True
        
        #ambas casillas tienen datos
        if v_capTotal == True and v_canSectores == True:
            #si ya hay sectores 
            id_estadio = self.__sectores_db.searchIdEstadiobyName(self.__sectores_ui.lineEdit_nombre.text()) 
            id_estadio = id_estadio[0]
            print(id_estadio)
            haySectores = self.__sectores_db.contarSectorByIdEstacion(id_estadio)
            print("HAY SECTORES:  ",haySectores)            
            if haySectores != []:
                contador =0
                #print(" hay sectores")
                for x in haySectores:
                    contador += 1  
                sec = contador
                #print(sec)

                #mensaje de cuantos sectores pues ingresar
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Se ingreso  :" + str(sec))
                msg.exec()               
            else:
                print("no hay sectores")
                #si no hay sectores
                resultado = int(cantidadTotal) // int(cantidadSector)    
                butacas = resultado // FILAS  
                print(resultado)
                print(butacas)           
                self.__sectores_ui.lineEdit_cantFilas.setText(str(FILAS))           
                self.__sectores_ui.lineEdit_cantButacas.setText(str(butacas))

                #Activa boton confirmar
                self.__sectores_ui.pushButton_confirmar.setEnabled(True)
        
    def confirmar(self):
        #Activar frame 
        self.__sectores_ui.frame_datosSector.setEnabled(True)
        self.__sectores_ui.lineEdit_color.setEnabled(False)
        self.__sectores_ui.lineEdit_precioSector.setEnabled(False)


        
    

    def insertSectores(self,color,nombre,precio,nombreEstadio):
        if color != "" and nombre != "" and precio != "" and nombreEstadio != "" :
                
            #selecciona id_estadio 
            id_estadio = self.__sectores_db.searchIdEstadiobyName(nombreEstadio) #TUPLA (ID,)
            id_ = id_estadio[0]    
             #eliminado
            eliminado = "No"
            
            filas = self.__sectores_db.filas(id_estadio[0])
            print("filas",filas)

            #butacas
            butacas = self.__sectores_ui.lineEdit_cantButacas.text()
            print(butacas) 
            if filas == []: #no se cargo nada en ese sector 
                print("TIENE QUE ENTRAR UNA SOLA VEZ")
                i = 0      
                fin = i + int(FILAS)
                inicio = i
                self.__sectores_db.insertSector(color,nombre,inicio,fin,precio,butacas,id_,eliminado)
                self.mostrarSectores(id_)
                #limpiar los edits 
                self.__sectores_ui.lineEdit_nombreSector.clear()
                self.__sectores_ui.lineEdit_color.clear()
                self.__sectores_ui.lineEdit_precioSector.clear()
            else: # ya hay algo cargado
                haySectores = self.__sectores_db.contarSectorByIdEstacion(id_) #tira vacio porque, estas llamando a los no eliminados
                print("Hay Sectores: ",haySectores)
                contador =0
                if haySectores: 
                    print("entro a sectores")                   
                    for x in haySectores:
                        contador += 1
                    sec = contador
                    #print("COUNT MENU PRINCIPAL: ",sec)           
                    sectoresRestantes = self.__sectores_ui.lineEdit_cantSectores.text()
                    
                    print(sectoresRestantes)
                    if sec < int(sectoresRestantes):
                        #  1dato (,) +1 dato [(,),(,)]         
                        #traerse cantidad filas                               
                        for x,y in reversed (filas):                    
                            break                
                        inicio = y + 1                
                        fin = inicio + int(FILAS)
                            
                        self.__sectores_db.insertSector(color,nombre,inicio,fin,precio,butacas,id_,eliminado)
                        self.mostrarSectores(id_)
                        #limpiar los edits 
                        self.__sectores_ui.lineEdit_nombreSector.clear()
                        self.__sectores_ui.lineEdit_color.clear()
                        self.__sectores_ui.lineEdit_precioSector.clear()
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Informacion")
                        msg.setText("")
                        msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                        msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                        msg.setInformativeText("Estadio con Sectores Completo")
                        msg.exec()
                        self.__sectores_ui.lineEdit_nombreSector.clear()
                        self.__sectores_ui.lineEdit_color.clear()
                        self.__sectores_ui.lineEdit_precioSector.clear()
            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Advertencia")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Warning) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Complete Todo los datos")
            msg.exec()
        
        
    def mostrarSectores(self,id_estadio):
        tabla_sectores = self.__sectores_ui.tableWidget_estadio
        sectores = self.__sectores_db.getSectoresByIdEstadio(id_estadio)   
        print("showSectores:", sectores)
        tabla_sectores.setRowCount(0)     
        if sectores:     
            for row, data in enumerate(sectores):                               
                    tabla_sectores.insertRow(row)
                    for colum, data in enumerate(data):        
                        tabla_sectores.setItem(row,colum,QtWidgets.QTableWidgetItem(str(data)))

    def seleccionarSector(self):
        nombreSector = self.__sectores_ui.lineEdit_nombreSector.text()
        nombre_estadio = self.__sectores_ui.lineEdit_nombre.text()
        id_estadio = self.__estadios_bd.searchIdByName(nombre_estadio)

        print("datos..",nombre_estadio,id_estadio)


        #global id_sector
        #id_sector = self.__sectores_db.IDsectorByName(nombreSector)  
        #print("id_sector seleccionar sector",id_sector)         
        
        tabla_sectores = self.__sectores_ui.tableWidget_estadio
        if tabla_sectores.currentItem() !=None:      
            nombre = tabla_sectores.currentItem().text() 
            print("seleccion:", nombre)
            global cod_sector            
            cod_sector = self.__sectores_db.IDsectorByName(nombre,id_estadio[0])
            sectorSpecific = self.__sectores_db.getSpecificSectorById(cod_sector[0])   
            print(cod_sector[0])                   
            if sectorSpecific:                    
                for x in sectorSpecific:
                    nombreSector = x[0]                     
                    colorSector = x[1]                   
                    precioSector= x[2]                 
                    break 
                self.__sectores_ui.lineEdit_nombreSector.setEnabled(True)  
                self.__sectores_ui.lineEdit_color.setEnabled(True)  
                self.__sectores_ui.lineEdit_precioSector.setEnabled(True)                 
                self.__sectores_ui.frame_datosSector.setEnabled(True)  
                self.__sectores_ui.lineEdit_nombreSector.setText(nombreSector)
                self.__sectores_ui.lineEdit_color.setText(colorSector) 
                self.__sectores_ui.lineEdit_precioSector.setText(str(precioSector))  
                self.__sectores_ui.pushButton_Est_Modificar.setEnabled(True)                        
                self.__sectores_ui.pushButton_Est_Eliminar.setEnabled(True)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("Informacion")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("El sector no se encuentra")
                msg.exec()

    

    def modificarSector(self,nombreSector,colorSector):
        #Para modificar primero no tiene que haber tickets vendidos en ese estadio,sector
        nombre_estadio = self.__sectores_ui.lineEdit_nombre.text()
        id_estadio = self.__estadios_bd.searchIdByName(nombre_estadio)
        global cod_sector
        sectoresVendidos = self.__tickets_bd.ticketsByNameSector_Estadio(id_estadio[0],cod_sector[0])
        print(sectoresVendidos)

        if sectoresVendidos:
            #no se puede modificar tiene tickets vendidos 
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("Informacion")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("El sector tiene tickets no se puede modificar")
            msg.exec()
        else:
            #verificar que en ese estadio no se repita el nombre del sector ni el color
            validar_Sector = self.__sectores_db.Color_NombreBy_Estadio(id_estadio[0])
            print(validar_Sector)
            if validar_Sector:
                if validar_Sector[0] == colorSector:
                    msg = QMessageBox()
                    msg.setWindowTitle("Informacion")
                    msg.setText("Informacion")
                    msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                    msg.setInformativeText("El color ya existe")
                    msg.exec() 
                #MENSAJE QUE TIENE QUE ELEGIR OTRO COLOR
                elif validar_Sector[1] == nombreSector:
                #MENSAJE QUE TIENE QUE ELEGIR OTRO NOMBRE
                    msg = QMessageBox()
                    msg.setWindowTitle("Informacion")
                    msg.setText("Informacion")
                    msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                    msg.setInformativeText("El nombre ya existe")
                    msg.exec()
                else:
                    #modifico
                    #el precio no se cambia
                    print("ID_____________",cod_sector)
                    self.__sectores_db.modificarSector(nombreSector,colorSector,cod_sector[0])
                    self.mostrarSectores(id_estadio[0])
    def eliminarSector(self):
        #ver si el sector tiene tiquets vendido 
        #si los tiene no se elimina
        nombre_estadio = self.__sectores_ui.lineEdit_nombre.text()
        id_estadio = self.__estadios_bd.searchIdByName(nombre_estadio)
        sectorSeleccionado = self.__sectores_db.getSpecificSectorById(cod_sector[0])
        print("sector seleccionado",sectorSeleccionado)

        tickets = self.__tickets_bd.sectoresVendidosByestadioId(id_estadio[0])
        print("tickets", tickets)
        if tickets:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("Informacion")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Posee tickets vendidos, no se puede modificar")
            msg.exec()
        else:
            eliminado = "Si"
            print("cod:", cod_sector[0])
            self.__sectores_db.eliminarSector(eliminado,cod_sector[0])
            self.__sectores_ui.lineEdit_nombreSector.clear()  
            self.__sectores_ui.lineEdit_color.clear()  
            self.__sectores_ui.lineEdit_precioSector.clear()
            self.mostrarSectores(id_estadio[0])

                    