import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

#importar todo lo que necesitamos
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta,time

from Database.conexion import conexion
from Models.Tickets import Tickets
from Models.Categorias import Categorias
from Models.Estadios import Estadios
from Models.Eventos import Eventos
from Models.Inscripciones import Inscrpciones
from Models.Tarifas import Tarifas
from Models.Sectores import Sectores

from reportlab.pdfgen import canvas
from reportlab.lib import colors
import webbrowser

from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyQt6.QtWidgets import QFileDialog
import qrcode
from PIL import Image



from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
import random

class Ticket_Control():  
    
    
    def __init__(self, ventana):
        self.__ticket_db = Tickets(conexion())   
        self.__ticket_ui = ventana
        self.__categoria_db = Categorias(conexion())   
        self.__eventos_db = Eventos(conexion())   
        self.__estadios_db = Estadios(conexion()) 
        self.__inscripciones_db = Inscrpciones(conexion()) 
        self.__tarifas_bd = Tarifas(conexion())
        self.__sectores_bd = Sectores(conexion())
        global contador
        global tablaTicketsAux
        global resultado
        resultado = 0.00
        tablaTicketsAux = []
        contador = 0
        

    def showWindowTicket(self,pantallaMostrar):
         #pasar a la otra pantalla
            #Ui_login.hide()
            self.__ticket_ui.Form = QtWidgets.QMainWindow()
            self.__ticket_ui.ui = pantallaMostrar()
            self.__ticket_ui.ui.setupUi(self.__ticket_ui.Form)
            self.__ticket_ui.Form.show()   
            
    def inicializarComboBoxCategorias(self):
        infoCombo = self.__categoria_db.cargarComboCategorias()         
        for item in infoCombo:
            for x in item:                              
                self.__ticket_ui.comboBox_categoria.addItem(x)
        

    def inicializarComboBoxEventos(self): 
        infoCombo = self.__eventos_db.cargarComboEventosNombres()         
        for item in infoCombo:
            for x in item:                              
                 self.__ticket_ui.comboBox_evento.addItem(x)     

    def inicializarComboBoxNombres(self):
        self.__ticket_ui.comboBox_nombre.clear()
        cadena = self.__ticket_ui.comboBox_categoria.currentText()
        infoCombo = self.__inscripciones_db.cargarComboNombres(cadena)         
        for item in infoCombo:
            for x in item:                              
                self.__ticket_ui.comboBox_nombre.addItem(x)  

    def inicializarComboBoxEstadio(self): 
        self.__ticket_ui.comboBox_lugar.clear()
        cadena = self.__ticket_ui.comboBox_evento.currentText()
        #print(cadena)
        infoCombo = self.__eventos_db.cargarComboEstadiosNombres(cadena) 
        #print(infoCombo)        
        for item in infoCombo:
            for x in item:                              
                 self.__ticket_ui.comboBox_lugar.addItem(x)  
                   
    def rangofechas(self, desde, hasta):        
        rango = []
        # Calculamos la diferencia de los días
        dias_totales = (hasta - desde).days
        for days in range(dias_totales + 1): 
            fecha = desde + relativedelta(days=days)
            rango.append(fecha)
        return rango

    def inicializarComboBoxFechas(self):
        self.__ticket_ui.comboBox_fecha.clear()
        global eventoSeleccionado 
        eventoSeleccionado = self.__ticket_ui.comboBox_evento.currentText()      
       
        if eventoSeleccionado:
            global id_evento
            id_evento = self.__eventos_db.getIdEventoSpecific(eventoSeleccionado)
             #tengo que traer las dos fechas del evento que se haya seleccionado
            fechaInicio = self.__eventos_db.getDateInicio(id_evento)
            fechaFin = self.__eventos_db.getDateFinal(id_evento)           
            infoCombo =self.rangofechas(fechaInicio,fechaFin)
            
            for item in range(len(infoCombo)):                                            
                self.__ticket_ui.comboBox_fecha.addItem(str(infoCombo[item]))    
    
    def inicializarComboBoxTipoEntrada(self):
        infoCombo = self.__tarifas_bd.cargarComboBox()         
        for item in infoCombo:
            for x in item:                              
                self.__ticket_ui.comboBox_tipoEntrada.addItem(x) 

    def iniciliazarPrecio(self):
        self.__ticket_ui.lineEdit_precio.clear() 
        cadena = self.__ticket_ui.comboBox_tipoEntrada.currentText()
        infoEdit = self.__tarifas_bd.precioByTipo(cadena)
        print(infoEdit)

        self.__ticket_ui.lineEdit_precio.setText(str(infoEdit[0]))

         

    def inicializarComboCantidad(self):
        infoCombo = ["1"]         
        for item in infoCombo:                                       
                self.__ticket_ui.comboBox_cantidad.addItem(item) 
    
    def inicializarComboBoxSectores(self):
        self.__ticket_ui.comboBox_sector.clear()
        cadena = self.__ticket_ui.comboBox_lugar.currentText()
        #print(cadena)
        idEstadio = self.__estadios_db.searchIdByName(cadena)
        print(idEstadio) #(5,)
        infoCombo = self.__sectores_bd.cargarComboBoxNoEliminados(idEstadio[0])  
          
        for item in infoCombo:
                    for x in item: 
                        print(x)                             
                        self.__ticket_ui.comboBox_sector.addItem(x)
                        break
        
        

    def inicializarComboBoxFila(self):
        self.__ticket_ui.comboBox_fila.clear()
        cadena = self.__ticket_ui.comboBox_sector.currentText()
        infoCombo = self.__sectores_bd.cargarComboBoxFila(cadena)  
        filaInicio = infoCombo[0][0]
        filaFin = infoCombo[0][1]
        precio = infoCombo[0][2]
       
        self.__ticket_ui.lineEdit_idTickets_3.setText(str(precio))
        for filaInicio in range(filaInicio,filaFin+1):               
                self.__ticket_ui.comboBox_fila.addItem(str(filaInicio))
               

    def inicializarComboBoxButaca(self): 
        sector = self.__ticket_ui.comboBox_sector.currentText() 
        butacas = self.__sectores_bd.getButacas(sector)
        print("butacas: ", butacas)
        if butacas != None:
            for item in range (1,butacas[0]+1):                                       
                self.__ticket_ui.comboBox_butacas.addItem(str(item)) 
        else:
            msg = QMessageBox()                
            msg.setWindowTitle("Advertencia")
            msg.setText("Problema de Asignacion")
            msg.setIcon(QMessageBox.Icon.Warning) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("El Estadio no tiene asignados sectores,ingreselos en Estadio")
            msg.exec()
    
    def mostrarGrilla(self):
       
        tabla_ticketsGeneral = self.__ticket_ui.tableWidget_alla_tickets
        
        ticketsEmitidos = self.__ticket_db.showTicketsSoul()       
        #TRAE LOS IDS HAY QUE GENERAR UNA NUEVA LISTA CON LAS DESCRIPCIONES
       
        listaDescripciones = []
        if ticketsEmitidos != None:
            for lista in ticketsEmitidos:
                #print(lista) 
                cod = lista [0]
                #print(cod)
                dia = lista[1]            
                #print(dia)            
                id_sector = lista[2]
                nombre_sector = self.__sectores_bd.getNameById(id_sector)
                print(nombre_sector)
                color = self.__sectores_bd.colorByID(id_sector)
                #print(color[0])
                fila = lista[3]
                #print(fila)
                butaca = lista[4]
                #print(butaca)
                cantidad = lista [5]
                #print(cantidad)
                id_tipoEntrada = lista[6]
                #print(id_tipoEntrada)
                #print(lista[7])
                #print(lista[8])
                id_nombre = lista[9]
                #print(id_nombre)
                id_evento = lista[10]
                #print(id_evento)
                id_festival = lista[11]
                #print(id_festival)
                #buscar las descripciones e insertarlo en la lista
                #print("####################################")
                sectorDescripcion = self.__sectores_bd.getNameById(id_sector)
                print(sectorDescripcion[0])
                tipoEntradaDescripcion = self.__tarifas_bd.getNameById(id_tipoEntrada)
                #print(tipoEntradaDescripcion[0])
                nombreDescripcion = self.__inscripciones_db.getNameById(id_nombre)
                #print(nombreDescripcion[0])
                eventoDescripcion = self.__estadios_db.getNameEventoById(id_evento)
                #print(eventoDescripcion)
                festivalDescripcion = self.__eventos_db.getNameFestivalById(id_festival)
                #print(festivalDescripcion)
                listaDescripciones.extend([[str(cod),str(dia),sectorDescripcion[0],color[0],str(fila),str(butaca),str(cantidad),tipoEntradaDescripcion[0],str(lista[7]),str(lista[8]),nombreDescripcion[0],eventoDescripcion[0][0],festivalDescripcion[0][0]]])

            #print("LISTA DESCRIPCIONES: ",listaDescripciones)
            if listaDescripciones != []:             
                self.__ticket_ui.pushButton_seleccionar.setEnabled(True)
                for row,data in enumerate(listaDescripciones):                               
                        tabla_ticketsGeneral.insertRow(row)
                        for colum,data in enumerate(data):        
                            tabla_ticketsGeneral.setItem(row,colum,QtWidgets.QTableWidgetItem(str(data)))  

   
   
    def agregarGrilla(self,tipoEntrada,precioUnitario,cantidad,sector,fila,butaca):
        global contador,tablaTicketsAux    
        #print("TA:",tablaTicketsAux)   
        grilla = self.__ticket_ui.tableWidget_tickets
        cadena= self.__ticket_ui.comboBox_sector.currentText()
        bandera = True      
        
        #Si hay datos en blanco
        if tipoEntrada != "" and precioUnitario != "" and cantidad != "" and sector!= "" and fila != ""  and butaca != "" :
            
            #CHEQUEAR QUE NO ESTE LA FILA,BUTACA,SECTOR,FECHA Y EVENTO EN LA BASE DE DATOS
            #YA SE VENDIO
            #fecha seleccionada
            fecha_chequeo = self.__ticket_ui.comboBox_fecha.currentText()
            
            evento = self.__ticket_ui.comboBox_lugar.currentText()   
            id_evento = self.__estadios_db.searchIdByName(evento) 
            print("id evento:",id_evento[0])


            #sector seleccionado
            sector_chequeo = self.__ticket_ui.comboBox_sector.currentText()
            print(sector_chequeo)
            sector_chequeo_id = self.__sectores_bd.id_eventoYnombre(id_evento[0],sector_chequeo)
            print("sector_id",sector_chequeo_id)

            

            nombre = self.__ticket_ui.comboBox_nombre.currentText()
            id_nombre = self.__inscripciones_db.getIdByName(nombre)

            if sector_chequeo_id:
                verificarAnteriores = self.verificarTicketsvendidos(sector_chequeo_id[0],fecha_chequeo,fila,butaca,id_evento[0],id_nombre[0])
                #print("verificarAnteriores:", verificarAnteriores)


                if verificarAnteriores == []: 
                    #no se vendio la fila,butaca,sector,en ese evento ese dia
                    msg = QMessageBox()                
                    msg.setWindowTitle("Informacion")
                    msg.setText("Verifique que los datos sean correctos - FILA - SECTOR - BUTACA")
                    msg.setIcon(QMessageBox.Icon.Warning) #Critical,Warning,Information
                    msg.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.Cancel) #"Cancel,"war,close,yes,not,retry            
                    msg.setInformativeText("Una vez ingresados NO podra modificarlos" + " Debera ELIMINAR el ticket y generar uno nuevo")
                    ret = msg.exec()

                    if ret == 0x00400000: #Cancel
                        print("cancel")                                       
                    elif ret == 0x00004000: #Yes 
                        #COLOCA EN LA GRILLA DE ABAJO                     
                        precioSector = self.__sectores_bd.precioSector(cadena)
                        precio = (float(precioUnitario) * int(cantidad)) + float(precioSector[0])
                        #print("Precio = cantidad * precioUni: ",precio)                    
                        grilla.setRowCount(contador)
                        lista = [(tipoEntrada,cantidad,precio,sector,fila,butaca)] 
                        print("L",lista)   
                        
                        #VERIFICA QUE NO ESTE YA EN LA GRILLA
                        if tablaTicketsAux != []: #la grilla ya tiene datos
                            for x in tablaTicketsAux:            
                                for y in x: 
                                    print("Y",y)               
                                    if y[4] == lista[0][4] and y[5] == lista[0][5]:
                                        bandera = False
                                        msg = QMessageBox()
                                        msg.setWindowTitle("Advertencia")
                                        msg.setText("Verificar")
                                        msg.setIcon(QMessageBox.Icon.Critical) #Critical,Warning,Information
                                        msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                                        msg.setInformativeText("FILAS y BUTACAS ya seleccionadas anteriormente")
                                        msg.exec()
                                        break              
                                break
                        
                        if bandera == True:           
                                for row,data in enumerate(lista):                               
                                    grilla.insertRow(row)
                                    for colum,data in enumerate(data):        
                                                grilla.setItem(row,colum,QtWidgets.QTableWidgetItem(str(data)))                         
                                    contador += 1
                                    valor = lista[0][2]
                                tablaTicketsAux.append(lista)
                                self.calcularTotal(valor)#ir haciendo la cuenta de ticket TOTAL
                else:
                    # Ya se vendio la fila,butaca,sector,en ese evento ese dia
                    msg = QMessageBox()
                    msg.setWindowTitle("Advertencia")
                    msg.setText("")
                    msg.setIcon(QMessageBox.Icon.Critical) #Critical,Warning,Information
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                    msg.setInformativeText("El Sector " + str(sector)+ " en la Fila: " + str(fila)+ " , Butaca: " +str(butaca)+ " el dia seleccionado ya fueron vendidos")
                    msg.exec()    
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Advertencia")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Critical) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("El sector no tiene Asignado Fila ni Sector")
                msg.exec()   


        else:
            msg = QMessageBox()
            msg.setWindowTitle("Advertencia")
            msg.setText("")
            msg.setIcon(QMessageBox.Icon.Critical) #Critical,Warning,Information
            msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
            msg.setInformativeText("Faltan Datos")
            msg.exec()
           

    def calcularTotal(self,valor):
        global resultado        
        resultado = resultado  + valor        
        self.__ticket_ui.lineEdit__total.setText(str(resultado))
        
    def seleccionarGrilla(self):
        self.__ticket_ui.lineEdit_idTickets.clear()
        tabla_general = self.__ticket_ui.tableWidget_alla_tickets
        if tabla_general.currentItem() != None:   

            self.__ticket_ui.pushButton_eliminar.setEnabled(True)
            self.__ticket_ui.pushButton_imprimir.setEnabled(True)
             
            
            cod = tabla_general.currentItem().text()    
            print(cod)                 

            
            id_ticket = self.__ticket_db.selectCod_TicketByID(cod)  
            #print("id: ",id_inscripcion) #anda 1           

            if id_ticket != None:  #presiono el nombre
                global specific_id   #se usa solamente para eliminar
                specific_id = id_ticket[0][1]
                specific_cod = id_ticket [0][0] 
                print(specific_id)

                if specific_id:
                     self.__ticket_ui.lineEdit_idTickets.setText(str(specific_cod)) 
               
    

    def verificarTicketsvendidos(self,sector,dia,fila,butaca,evento,banda):      
        yaVendidos = self.__ticket_db.verificarEntradaByFilaButacaSectorFechaEvento(fila,butaca,sector,dia,evento,banda)
        return yaVendidos

    def removeRowsTablaAllTicket(self):   
        if self.__ticket_ui.tableWidget_alla_tickets.rowCount() > 0:
                self.__ticket_ui.tableWidget_alla_tickets.removeRow(self.__ticket_ui.tableWidget_alla_tickets.rowCount()-1)
    
    def removeRowsTablaTicket(self):   
        if self.__ticket_ui.tableWidget_tickets.rowCount() > 0:
                self.__ticket_ui.tableWidget_tickets.removeRow(self.__ticket_ui.tableWidget_tickets.rowCount()-1)

    def ingresar(self,lugar,fecha,categoria,nombre,sector,fila,butaca,tipoEntrada,preciototal):
            eliminado = "No"
            global tablaTicketsAux
            #print(tablaTicketsAux)             
            if fecha != "" and categoria != "" and nombre != "" and sector != "" and fila != "" and butaca != "" and tipoEntrada != "" and preciototal != "":
                cod = random.randint(1, 15000)            
                #verificar que el codigo no este ya ingresado
                codigos = self.__ticket_db.codigosNoUsado(cod)            
                while codigos != []:
                    cod = random.randint(1, 15000)          
                
                cantidad = 1
                #Querys para traer ids     
                    
                evento = self.__ticket_ui.comboBox_lugar.currentText()   
                id_evento = self.__estadios_db.searchIdByName(evento)
                print("id_evento ",id_evento[0]) 

                festival = self.__ticket_ui.comboBox_evento.currentText()           
                id_festival = self.__eventos_db.getIdEventByLugar(evento,festival)            
                print("id_festival: ",id_festival)      

                id_nombre = self.__inscripciones_db.getIdInscripcionSpecific(nombre)
                #print("id_banda: ",id_nombre)
                id_categoria = self.__categoria_db.getCategoriaSpecific(categoria)
                #print("categoria: ",id_categoria[0])

                for lista in tablaTicketsAux:
                    for item in lista:                    
                        #print(item)
                        tipoEntrada = item[0]
                        #print(tipoEntrada)
                        cantidad = item[1]                    
                        #print(cantidad)
                        sector = item[3]
                        #print(sector)                  
                        fila = item[4]
                        #print("fila: ",fila)
                        butaca = item [5]
                        #print("butaca:",butaca)
                        precioEntrada = self.__tarifas_bd.searchTarifaByName(tipoEntrada)
                        #print("precio Entrada",precioEntrada[2])
                        precioSector = self.__sectores_bd.precioSector(sector)
                        #print("precio_sECTOR:",precioSector[0])
                        print(id_evento[0],"----",sector)
                        id_sector = self.__sectores_bd.id_eventoYnombre(id_evento[0],sector) 
                        print("sector id: ",id_sector)
                        id_tipoEntrada = self.__tarifas_bd.getIdTarifaSpecific(tipoEntrada)
                        #print("tipo_entrada",id_tipoEntrada[0])
                        #print("FECHA",fecha)                 
                        self.__ticket_db.ingresar(cod,id_festival[0][0],id_evento[0],fecha,id_categoria[0],id_nombre,id_sector[0],fila,butaca,precioSector[0],id_tipoEntrada[0],precioEntrada[2],cantidad,preciototal, eliminado)
                        continue
                    
                self.removeRowsTablaTicket()
                self.__ticket_ui.lineEdit__total.clear()
                self.mostrarGrilla()
                msg = QMessageBox()
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Information) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Tickets Guardados - IdTicket " + str(cod))
                msg.exec()


    def eliminar(self):
        eliminado = "Si"

        cod = self.__ticket_ui.lineEdit_idTickets.text()
        print(cod)

        ticketSeleccionado = self.__ticket_db.ticketUpdateEliminar(cod)      
        print(" TICKET SELECCIONADO ",ticketSeleccionado)
        
        for item in ticketSeleccionado:             
            print(item)            
            id_ = item[0]                       
            #festival = x[1]                
            #lugar = x[2]               
            #nombre = x[3]                
            fila = 0                 
            butaca = 0
            #sector =x[6] 
            self.__ticket_db.eliminar(fila,butaca,id_,eliminado)
            self.removeRowsTablaAllTicket()
            self.mostrarGrilla()
        
        self.__ticket_ui.lineEdit_idTickets.clear()



    def generarPDF(self):
        bandera = False   
        global specific_id
        #print("id del registro seleccionado: ",specific_id)      
        
        #generar el ticket       
        id_entrada = specific_id
       
        #query con todos los datos que quiero que vayan en el ticked
        entrada_data = self.__ticket_db.pdf(id_entrada)
        #print(entrada_data)
        #[(20, 14691, 12, 5, datetime.datetime(2023, 11, 27, 0, 0), 5, 4, 33, 7, 8, Decimal('1000.00'), 26, Decimal('700.00'), 1, Decimal('1700.00'), 'No')]
        #con los ID's, obtener nuevamente los datos para imprimirlos
        
        for item in entrada_data:
                #print(item)
                idTicket = item[1]           
                #print(idTicket)
                festivalNombreid = item[2]           
                festivalNombre = self.__eventos_db.getNameFestivalById(festivalNombreid)
                #print(festivalNombre[0])
                lugarFestivalid = item[3]
                lugarFestival = self.__estadios_db.getNameEventoById(lugarFestivalid)
                #print(lugarFestival[0][0])
                dia = item[4]
                #print(dia)
                horario = self.__eventos_db.getHoraInicial(festivalNombreid)
                #print(horario)
                categoriaID = item[5]
                categoria = self.__categoria_db.getNameCategoriaByID(categoriaID)
                #print(categoria[0])                
                nombreBandaid=item[6]
                nombreBanda = self.__inscripciones_db.getNameById(nombreBandaid)
                #print(nombreBanda[0])
                sectorID=item[7]
                sectorColor = self.__sectores_bd.colorByID(sectorID)
                sectorNombre = self.__sectores_bd.getNameById(sectorID)
                #print(sectorColor[0], sectorNombre[0])         
                fila=item[8]
                #print(fila)
                butaca = item[9]
                #print( butaca)
                precioSector = item[10]
                #print(precioSector)
                tipoEntradaID = item[11]
                tipoEntrada = self.__tarifas_bd.getNameById(tipoEntradaID)
                #print(tipoEntrada[0])
                precioEntrada = item[12]  
                #print(precioEntrada)
                cantidad = item[13]
                #print(cantidad)
                precioTotalTicked = item[14]
                #print(precioTotalTicked)
                
                                    
       
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)        
        file_dialog.setDefaultSuffix(".pdf")
        file_dialog.setNameFilter("Archivos PDF (*.pdf)")

        # Obtener la ruta del archivo seleccionada por el usuario        
        file_path, _ = file_dialog.getSaveFileName(None, "Guardar como", "Ticket "+str(idTicket)+".pdf", "Archivos PDF (.pdf);;Todos los archivos ()")

        # Verificar si el usuario ha cancelado la selección    
        if file_path:
        # Continuar con la generación del PDF usando la ruta seleccionada
            pdf_file_path = file_path
       
        #aux = datetime.date(dia)
        # Genera codigo qr       
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=5,
        )
        
        qr_data = f"Festival:{festivalNombre[0]}\nLugar: {lugarFestival[0][0]}\nBanda: {nombreBanda[0]}\nFecha: {dia}\nHorario: {horario}\nSector: {sectorNombre[0]}\nSector Color: {sectorColor[0]}\nFila: {fila}\nButaca: {butaca}\nTipo Entrada: {tipoEntrada[0]}\nPrecio Ticket: ${precioTotalTicked}\nIdTicket: {idTicket}"                
       
                        

        qr.add_data(qr_data)
               
        qr.make(fit=True)
        #qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img = qr.make_image(
            fill_color="black",
            back_color="white")
        
        qr_path = f"QR_ {specific_id}.png" 
        qr_img.save(qr_path)
                
        try: 
            open(pdf_file_path, 'wb')
            bandera = True    
        except:
                msg = QMessageBox()                
                msg.setWindowTitle("Informacion")
                msg.setText("")
                msg.setIcon(QMessageBox.Icon.Warning) #Critical,Warning,Information
                msg.setStandardButtons(QMessageBox.StandardButton.Ok) #"Cancel,"war,close,yes,not,retry            
                msg.setInformativeText("Verifique tener el archivo cerrado.")
                msg.exec()
        
        if bandera == True:
            with open(pdf_file_path, 'wb') as pdf_file:
                c = canvas.Canvas(pdf_file, pagesize=A4)         
                
                # Agregar titulo con color y formato (azul marino)
                c.setFont("Helvetica", 15)  
                c.setFillColorRGB(0, 0, 0)  
                c.drawCentredString(150, 750, " " + str(festivalNombre[0]))

                # Agregar código QR al ticket			
                c.drawInlineImage(qr_path, 78, 575, width=130, height=130)
            

                # color y tamaño de la tabla
                c.setFillColorRGB(0, 0, 0)  
                c.setFont("Helvetica", 16)  
                
                #Textos                              
                text = c.beginText(80,500 )
                text.setFont("Helvetica", 13)
                text.textLine("Lugar :" + str(lugarFestival[0][0]))
                text.textLine("Evento: " + str(nombreBanda[0]))                 
                text.textLine("Fecha: " + str(dia))                               
                c.drawText(text)

                #TEXTO HORA
                text_horario = c.beginText(250,470 )
                text_horario.setFont("Helvetica", 13)
                text_horario.textLine("Hora :" + str(horario))                                              
                c.drawText(text_horario)

                #texto de Sector 
                text_sector = c.beginText(80,440 )
                text_sector.setFont("Helvetica", 13)
                text_sector.textLine("Sector : " + str(sectorNombre[0])) 
                text_sector.textLine("Color : " + str(sectorColor[0]))                                             
                c.drawText(text_sector)

                #texto de Fila 
                text_fila = c.beginText(210,440)
                text_fila.setFont("Helvetica", 13)
                text_fila.textLine("Fila :" + str(fila))                                              
                c.drawText(text_fila)

                #texto de Butaca
                text_butaca = c.beginText(270,440)
                text_butaca.setFont("Helvetica", 13)
                text_butaca.textLine("Butaca :" + str(butaca))                                              
                c.drawText(text_butaca)

                #texto de TipoEntrada y precio
                text_tipoEntrada = c.beginText(80,400 )
                text_tipoEntrada.setFont("Helvetica", 13)
                text_tipoEntrada.textLine("Tipo de Entrada: " + str(tipoEntrada[0]))  
                text_tipoEntrada.textLine("Precio: $ " + str(precioEntrada)) 
                text_tipoEntrada.textLine("Precio Total: $ " + str(precioTotalTicked))                                           
                c.drawText(text_tipoEntrada)
                #idTicket
                text_id = c.beginText(80,300)
                text_id.setFont("Helvetica", 13)
                text_id.textLine("IdTicket :" + str(idTicket))                                                              
                c.drawText(text_id)                

                # Guarda y cierra el archivo PDF
                c.save()                
                # Abre el navegador con el archivo PDF
                try:
                    webbrowser.open(pdf_file_path)
                except Exception as e:
                    QMessageBox.information(self, 'Error', f'Error opening PDF: {str(e)}')




