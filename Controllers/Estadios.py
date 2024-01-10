import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos
from Database.conexion import conexion
from Models.Estadios import Estadios
from Models.Sectores import Sectores
from Models.Tickets import Tickets
from Controllers.Sectores import Sector_Control

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
MAYUS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CARACTER_ESPECIAL = ["$","%","&","#"," ","!","/","*",",",".","@","(",")","=","?","¡","¿","<",">"]
NUM =   ["0","1","2","3","4","5","6","7","8","9"]

class Estadio_Control():

    global id_estadio
    
    def __init__(self, ventana):
        self.__estadios_db = Estadios(conexion()) 
        self.__sectores_db = Sectores(conexion())  
        self.__estadios_ui = ventana
        self.__sectorControl = Sector_Control(ventana)
        self.__tickets__bd = Tickets(conexion())
       
    def sectoresActuales(self):
        return cantSectoresActualesEstadio
    
    def sectoresRestantes(self):
        return sectoresRestantes

    def validarCadenaNombre(self):        
        cadena = self.__estadios_ui.lineEdit_nombre.text()        
        valido = False
        for x in cadena:
            if x in MAYUS:
                valido = True

        if valido == True:            
            self.buscarEstadio(cadena)
            id_estadio = self.__estadios_db.searchIdByName(cadena)
            print(id_estadio)            
           
            if id_estadio:
                id_estadio_int = id_estadio[0]     
                if id_estadio_int:                                  
                    sectores = self.searchSectores(id_estadio_int)
                    print(sectores) 
                    if sectores:
                        
                        self.__sectorControl.mostrarSectores(id_estadio_int)
                        self.__estadios_ui.pushButton_Est_Seleccionar.setEnabled(True)
                        sector = self.__sectores_db.getSectoresByIdEstadio(id_estadio_int)                        
                        for x in sector:
                            for y in x:                                
                                filaInicio = x[2]
                                filaFin = x[3]
                                butacas = x[4]
                                break
                     
                        #cantidad de sectores ya cargado del estadio
                        sectorActuales = self.__sectores_db.contarSectorByIdEstacion(id_estadio_int) 
                        global cantSectoresActualesEstadio
                        cantSectoresActualesEstadio = sectorActuales[0]
                        #print("Sector Actual:",cantSectoresActualesEstadio)


                        #traerse cantTotal
                        total = self.__estadios_ui.lineEdit_capTotal.text()
                        filasTotalSector = int(filaFin) - int(filaInicio)
                        #print(filasTotalSector)
                        self.__estadios_ui.lineEdit_cantFilas.setText(str(filasTotalSector))
                        self.__estadios_ui.lineEdit_cantButacas.setText(str(butacas))

                        #Saber cantidad de sectores restantes
                        filasRestantes = int(total) // int(filasTotalSector)
                        
                        global sectoresRestantes
                        sectoresRestantes = (filasRestantes // int(butacas))

                        self.__estadios_ui.lineEdit_cantSectores.setText(str(sectoresRestantes))
                        self.__estadios_ui.pushButton_confirmar.setEnabled(True)
                        msg = QMessageBox()
                        msg.setWindowTitle("Informacion")
                        msg.setText("")
                        msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                        msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                        msg.setInformativeText("Presione ENTER en CONFIRMAR")
                        msg.exec()  
                    else:                       
                        self.__estadios_ui.lineEdit_cantSectores.clear()
                        self.__estadios_ui.lineEdit_cantButacas.clear()
                        self.__estadios_ui.lineEdit_cantFilas.clear()
                        #self.__estadios_ui.tableWidget_estadio.
                        msg = QMessageBox()
                        msg.setWindowTitle("Informacion")
                        msg.setText("Estadio sin Asignacion")
                        msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                        msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                        msg.setInformativeText("No posee asignado Sectores ni Filas")
                        msg.exec() 
        else:
            #limpiar los edits, y tabla.
            self.__estadios_ui.lineEdit_nombre.clear() 
            self.__estadios_ui.lineEdit_direccion.clear()
            self.__estadios_ui.lineEdit_telefono.clear()  
            self.__estadios_ui.lineEdit_correo.clear()
            self.__estadios_ui.lineEdit_capTotal.clear()
            self.__estadios_ui.lineEdit_cantSectores.clear()
            self.__estadios_ui.lineEdit_cantButacas.clear()
            self.__estadios_ui.lineEdit_cantFilas.clear()
            #self.__estadios_ui.tableWidget_estadio.
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Solo Letras")
            msg.exec()
                  
                





    def validarCadena(self,cadena):
        for x in cadena:
            if x in MAYUS:
                return True
            
    def validarNumeros(self,cadena):
        for x in cadena:
            if x in NUM:
                return True
            
    def validarTodo(self,cadena):
        contador = 0
        tamaño = len(cadena) 
        #print(cadena)
        #print(tamaño)      
        for x in cadena:
            #print(x)            
            if x in NUM:
                contador +=1
            if x in MAYUS:
                contador +=1
            if x in CARACTER_ESPECIAL:
                contador +=1
        #print(contador)
        if contador == tamaño:
            return True
        
    def validarNumCaracter(self,cadena):
        contador = 0
        tamaño = len(cadena)
        for x in cadena:
            if x in NUM:
                contador +=1
            if x in MAYUS:                   
                contador +=1
        if contador == tamaño:
            return True

    def Limpiar_EditsEstadios(self):
        self.__estadios_ui.lineEdit_nombre.clear()
        self.__estadios_ui.lineEdit_telefono.clear()
        self.__estadios_ui.lineEdit_capTotal.clear()
        self.__estadios_ui.lineEdit_direccion.clear()
        self.__estadios_ui.lineEdit_correo.clear()

    def insertEstadio(self,nombre,direccion,telefono,correo,capTotal):       

        v_nom = self.validarCadena(nombre)
        v_dir = self.validarTodo(direccion)
        v_tel = self.validarNumeros(telefono)
        v_capTotal = self.validarNumeros(capTotal)
        v_correo = self.validarTodo(correo)
        print(v_nom)
        print(v_dir)
        print(v_tel)
        print(v_capTotal)
        print(v_correo)


        #print(v_nom,v_dir,v_tel,v_capTotal,v_correo)
        if nombre != "" and direccion != "" and telefono != "" and correo != "" and capTotal != "" :            
            if v_nom == True and v_dir == True and v_tel == True and v_capTotal == True and v_correo == True:
                self.__estadios_db.insert(nombre,direccion,telefono,correo,capTotal)   
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Estadio dado de Alta")
                msg.exec()


        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Complete y/o Verifique todos los campos")
            msg.exec()
           
        
    def buscarEstadio(self,nombre):
        resultado = self.__estadios_db.searchByName(nombre)
        global id_estadio
        id_estadio = self.__estadios_db.searchIdByName(nombre) 
        print(id_estadio)         
        #print(resultado)
        if resultado:
            self.__estadios_ui.lineEdit_nombre.setText(resultado[1])
            self.__estadios_ui.lineEdit_telefono.setText(str(resultado[4]))
            self.__estadios_ui.lineEdit_capTotal.setText(str(resultado[5]))
            self.__estadios_ui.lineEdit_direccion.setText(resultado[2])
            self.__estadios_ui.lineEdit_correo.setText(resultado[3])


            self.__estadios_ui.pushButton_estadioModificar.setEnabled(True)
            self.__estadios_ui.pushButton_estadioEliminar.setEnabled(True)
            #dar de alto la parte de cant de sectores 
            # el boton verificar y el edit de cant sectores
            self.__estadios_ui.lineEdit_cantSectores.setEnabled(True)
            

            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Estadio encontrado, puede modificarlo")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Estadio no encontrado")
            msg.exec()


    def modificarEstadio(self,nombre,direccion,telefono,correo,capTotal):
        print("entra")
        v_nom = self.validarCadena(nombre)
        v_dir = self.validarTodo(direccion)
        v_tel = self.validarNumeros(telefono)
        v_capTotal = self.validarNumeros(capTotal)
        v_correo = self.validarTodo(correo)
       

        if nombre != "" and direccion != "" and telefono != ""  and capTotal != "" : 
                print("entraaaaaa")           
                if v_nom == True and v_dir == True and v_tel == True and v_capTotal == True :
                    id_estadio = self.__estadios_db.searchIdByName(nombre)
                    print("MODIFICAR. ESTADIO:",id_estadio[0])
                    #VERIFICAR QUE NO TENGA TICKETS VENDIDO
                    tickets = self.__tickets__bd.ticketsVendidosByID_ESTADIO(id_estadio[0])
                    print(tickets)

                    if tickets:
                        #no se puede modificar
                        msg = QMessageBox()
                        msg.setWindowTitle("Informacion")
                        msg.setText("")
                        msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                        msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                        msg.setInformativeText("Estadio con tickets vendido, no se puede Modificar")
                        msg.exec()
                    else:   
                        print("entraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                        id_estadio = self.__estadios_db.searchIdByName(nombre)
                        print("MODIFICAR. ESTADIO:",id_estadio[0])
                        if id_estadio:
                            self.__estadios_db.modificar(direccion,telefono,correo,capTotal,id_estadio[0])   
                            self.Limpiar_EditsEstadios()
                            msg = QMessageBox()
                            msg.setWindowTitle("Informacion")
                            msg.setText("")
                            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                            msg.setInformativeText("Estadio Modificado")
                            msg.exec()

                        else:
                            msg = QMessageBox()
                            msg.setWindowTitle("Advertencia")
                            msg.setText("")
                            msg.setIcon(QMessageBox.Icon.Warning) #Critical,Warning,Information
                            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                            msg.setInformativeText("Estadio no encontrado")
                            msg.exec()


        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Complete y/o Verifique todos los campos")
            msg.exec()
        
    def eliminarEstadio(self):
        #verificar si tiene tickets vendidos 
        nombre= self.__estadios_ui.lineEdit_nombre.text()
        id_estadio = self.__estadios_db.searchIdByName(nombre)
        print("MODIFICAR. ESTADIO:",id_estadio[0])
        #VERIFICAR QUE NO TENGA TICKETS VENDIDO
        tickets = self.__tickets__bd.ticketsVendidosByID_ESTADIO(id_estadio[0])
        print(tickets)

        if tickets:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Estadio con tickets vendido no se puede eliminar")
            msg.exec()            
        else:
            print(id_estadio[0])
            ok = self.__estadios_db.eliminar(id_estadio[0])
            print(ok)
            if ok:
                self.Limpiar_EditsEstadios()
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Estadio Eliminado")
                msg.exec()
        
    def searchSectores(self,id_estadio):        
        sectores = self.__sectores_db.getSectoresByIdEstadio(id_estadio)   
        print("fin de la consulta",sectores)     
        return sectores
    
    def countSectores(self,id_estadio):
        #print("id_estadio count,",id_estadio)
        count = self.__sectores_db.contarSectorByIdEstacion(id_estadio)
        count_int = count[0]
        #print(count_int)
        return count_int
    
    def CantButacasByEstadio(self,id_estadio):
        butacas=self.__sectores_db.butacasByEstadio(id_estadio)
