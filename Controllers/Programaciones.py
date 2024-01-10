import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta,time
 
#importar todo lo que necesitamos
from Database.conexion import conexion
from Models.Programacion import Programacion
from Models.Categorias import Categorias
from Models.Eventos import Eventos
from Models.Inscripciones import Inscrpciones
from Models.Tickets import Tickets

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Programacion_Control():
    
    def __init__(self, ventana):
        self.__programacion_db = Programacion(conexion())   
        self.__programacion_ui = ventana
        self.__categoria_db = Categorias(conexion())   
        self.__eventos_db = Eventos(conexion())   
        self.__inscripciones_db = Inscrpciones(conexion()) 
        self.__tickets_db = Tickets(conexion())  


    def showWindowProgramaciones(self,pantallaMostrar):
         #pasar a la otra pantalla
            #Ui_login.hide()
            self.__programacion_ui.Form = QtWidgets.QMainWindow()
            self.__programacion_ui.ui = pantallaMostrar()
            self.__programacion_ui.ui.setupUi(self.__programacion_ui.Form)
            self.__programacion_ui.Form.show()  

    
    def inicializarComboBoxCategorias(self):
        infoCombo = self.__categoria_db.cargarComboCategorias()         
        for item in infoCombo:
            for x in item:                              
                self.__programacion_ui.comboBox_categorias.addItem(x)
        

    def inicializarComboBoxEventos(self):      
    
        
        infoCombo = self.__eventos_db.cargarComboEventosNombres()         
        for item in infoCombo:
            for x in item:                              
                 self.__programacion_ui.comboBox_eventos.addItem(x)   
    
    def inicializarComboBoxNombres(self):
        self.__programacion_ui.comboBox_nombres.clear()
        cadena = self.__programacion_ui.comboBox_categorias.currentText()
        print(cadena)       

        infoCombo = self.__inscripciones_db.cargarComboNombres(cadena)   
          
        for item in infoCombo:
            for x in item:                              
                self.__programacion_ui.comboBox_nombres.addItem(x)
    
    def rangofechas(self, desde, hasta):        
        rango = []
        # Calculamos la diferencia de los días
        dias_totales = (hasta - desde).days
        for days in range(dias_totales + 1): 
            fecha = desde + relativedelta(days=days)
            rango.append(fecha)
        return rango

    def inicializarComboBoxFechas(self):
        self.__programacion_ui.comboBox_dias.clear()
        global eventoSeleccionado 
        eventoSeleccionado = self.__programacion_ui.comboBox_eventos.currentText()        
        #print("eventoSeleccionado:",eventoSeleccionado)
        if eventoSeleccionado:
            global id_evento
            id_evento = self.__eventos_db.getIdEventoSpecific(eventoSeleccionado)
            #print(id_evento)

            #tengo que traer las dos fechas del evento que se haya seleccionado
            fechaInicio = self.__eventos_db.getDateInicio(id_evento)
            fechaFin = self.__eventos_db.getDateFinal(id_evento)           
            infoCombo =self.rangofechas(fechaInicio,fechaFin)
            
            for item in range(len(infoCombo)):                                            
                self.__programacion_ui.comboBox_dias.addItem(str(infoCombo[item]))            
               
           
    
    def horarioDisponibleByEvento(self,evento,dia,categoria):
        global horaInicioEvento
        ultimoHorario = self.__programacion_db.horarioDisponible(evento,dia,categoria) #lista  con los horarios de ese evento, de esa categoria y dia 
        horaInicioEvento = self.__eventos_db.getHoraInicial(id_evento)  
        print(horaInicioEvento)
        print("------seleccionan el nombre del artista------------------")
       
        if ultimoHorario:
            for item in reversed(ultimoHorario):
                print("item For: ",item[0])
                break
            
            horaResultado = item[0] + timedelta(hours=2) #cada presentacion tiene dos horas 
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Horario: " + str(horaResultado))        
            msg.exec() 
            return horaResultado
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("Horario: " +str(horaInicioEvento))
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("")        
            msg.exec() 
            return horaInicioEvento           
            
    
    def horarioDisponibleByEventoCargar(self,evento,dia,categoria):
        global horaInicioEvento
        ultimoHorario = self.__programacion_db.horarioDisponible(evento,dia,categoria)
        print(ultimoHorario)
        horaInicioEvento = self.__eventos_db.getHoraInicial(id_evento)
        print(horaInicioEvento)
        
        if ultimoHorario: #ya hay bandas cargadas para ese dia, tira el ultimo horario  + 2 horas
            for item in reversed(ultimoHorario):
                print(item)
                break          
            
            horaResultado = item[0] + timedelta(hours=2) #cada presentacion tiene dos horas 
            print("horarioDisponibleCargar",horaResultado)
            return horaResultado #el ultimo horario + 2 horas             
        else:    
            horaResultado =  horaInicioEvento      
            return horaResultado #retorna el primer horario
    
    
    
    def cargarProgramacion(self,evento,fecha,categoria,nombre):     
        
        #HORAS        
        horaResultado = self.horarioDisponibleByEventoCargar(evento,fecha,categoria) 
        #print("Cargar" + horaResultado)

        #QUE LA BANDA QUE SE ESTA POR DAR, NO ESTE DANDO EL MISMO DIA.
        banda_ok = self.__programacion_db.bandahabilitada(evento,fecha,categoria,nombre)       
 
        if banda_ok != []:            
            #ya esta ese dia
            self.showProgramacion()
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("Ya se encuentra el dia: " + fecha)
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Puede añadirla/o otro dia")        
            msg.exec() 
        else:                
            self.__programacion_db.cargarProgramacion(evento,fecha,categoria,nombre,horaResultado)
            self.showProgramacion()
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Agregada/o a la programacion")        
            msg.exec() 
    
    
    def showProgramacion(self):
        tabla_programacion = self.__programacion_ui.tableWidget_cronograma
        programacion = self.__programacion_db.getProgramacion()   
        #print("showCategories:",categorias)
        tabla_programacion.setRowCount(0)     
        if programacion:           
            for row, data in enumerate(programacion):                               
                    tabla_programacion.insertRow(row)
                    for colum, data in enumerate(data):        
                        tabla_programacion.setItem(row,colum,QtWidgets.QTableWidgetItem(str(data)))
    

    def seleccionar(self):
        tabla_programacion = self.__programacion_ui.tableWidget_cronograma
        
        if tabla_programacion.currentItem() != None:

            self.__programacion_ui.pushButton_eliminar.setEnabled(True)
            self.__programacion_ui.pushButton_modificar.setEnabled(True)  
            global id_programacion
            id_programacion = tabla_programacion.currentItem().text()    
            #print (id_programacion)               

            if id_programacion != None:  #presiono el nombre
                num = int(id_programacion)
                #print(type(num))
                programacionSpecific =  self.__programacion_db.get_programacionbyId(num)
                #print(programacionSpecific)  

                if  programacionSpecific :  #anda, pero tenes que tocar los cambo Box para que se activen las elecciones.
                    for x in  programacionSpecific :
                        y= x[1]
                        #print(y)
                        dt_obj = datetime.strptime(str(y),'%Y-%m-%d')
                        dt_str = datetime.strftime(dt_obj,'%Y-%m-%d' ) 
                        #print(dt_str)      
                        #print(x[3])               
                        self.__programacion_ui.comboBox_eventos.setCurrentText(x[0])
                        self.__programacion_ui.comboBox_dias.setCurrentText(dt_str)
                        self.__programacion_ui.comboBox_categorias.setCurrentText(x[2])
                        self.__programacion_ui.comboBox_nombres.setCurrentText(x[3])                  
                        break
        
            

    def modificar(self,evento,fecha,categoria,nombre):
        #controles 
        #print(fecha)
        #print("id_programacion: ", id_programacion)
        #ver si en el evento, el dia y la categoria, ellos (nombre) ya no tocan, si no tocan se los modifica si no chau
        valido_modificacion = self.__programacion_db.bandahabilitada(evento,fecha,categoria,nombre)
        #print(valido_modificacion)
        nombre_id = self.__inscripciones_db.getIdByName(nombre)
        #print("nombreid: ", nombre_id[0])
        #print(nombre)
        #print("evento",evento)
        #evento_id = self.__eventos_db.getIdEventByLugar(evento)
        evento_id = self.__eventos_db.getIdEventByName(evento)
        #print("id evento:",evento_id[0][0])
        valido_modificacionTicket = self.__tickets_db.ticket_Programacion(nombre_id[0],str(fecha),evento_id[0][0])
        #print(valido_modificacionTicket)
        if valido_modificacion != []:
            #print("entro a banda habilitada")
           #ya esta en ese evento 
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("Ya se encuentra exponiendo en este evento el dia seleccionado  ")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Puede añadirla/o otro dia")        
            msg.exec() 
        elif valido_modificacionTicket != None:
            #print("entro a tickets vendidos")    
            #si tiene tickest vendidos no se deja modificar
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("Posee tickets vendidos, no se puede modificar")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Puede añadirla/o otro dia")        
            msg.exec() 
        else:
            self.__programacion_db.modificar(evento,fecha,categoria,nombre,id_programacion)
            self.showProgramacion()
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("Programacion Modificada")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("")        
            msg.exec() 
    def eliminar(self):
        eliminado = "Si"
        print("id_programacion del seleccionar:",id_programacion)

        cadena = self.__programacion_db.get_programacionbyId(id_programacion)
        print(cadena)
        festival_nombre = cadena[0][0]
        print(festival_nombre)
        fecha = cadena[0][1]
        print(fecha)
        categoria =cadena[0][2]
        print(categoria)
        banda = cadena[0][3]
        print(banda)

        id_categoria = self.__categoria_db.getIdCategoriaSpecific(categoria)
        id_banda = self.__inscripciones_db.getIdByName(banda)
        id_festival = self.__eventos_db.getIdEventByName(festival_nombre)
        print("------------------------------")
        print(id_categoria)
        print(id_banda)
        print(id_festival)

        tickets_vendidos = self.__tickets_db.ticket_ProgramacionEliminar(id_festival[0][0],id_categoria[0],id_banda[0],str(fecha))
        print(tickets_vendidos)

        if tickets_vendidos: 
        #no sepuede eleiminar
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("No se puede eliminar")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Posee tickets vendidos")        
            msg.exec() 
        else:
            self.__programacion_db.eliminar(id_programacion,eliminado)
            self.showProgramacion()
            msg = QMessageBox()
            msg.setWindowTitle("Informacion")
            msg.setText("Programacion Eliminada")
            msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("")        
            msg.exec() 





























