
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate,QDate

from Controllers.Tickets import Ticket_Control


class Ui_Form_Tickets(object):
    def __init__(self):
        self.__tickets_controlles = Ticket_Control(self)
    def setupUi(self, Form_Tickets):
        Form_Tickets.setObjectName("Form_Tickets")
        Form_Tickets.resize(1317, 654)
        Form_Tickets.setMinimumSize(QtCore.QSize(1317, 654))
        Form_Tickets.setMaximumSize(QtCore.QSize(1317, 654))
        Form_Tickets.setStyleSheet("background-color: rgb(203, 203, 151);")
        self.comboBox_lugar = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_lugar.setGeometry(QtCore.QRect(360, 90, 281, 31))
        self.comboBox_lugar.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_lugar.setObjectName("comboBox_lugar")
        self.label = QtWidgets.QLabel(parent=Form_Tickets)
        self.label.setGeometry(QtCore.QRect(360, 70, 171, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 151, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_sector = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_sector.setGeometry(QtCore.QRect(20, 210, 81, 31))
        self.comboBox_sector.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_sector.setObjectName("comboBox_sector")
        self.comboBox_tipoEntrada = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_tipoEntrada.setGeometry(QtCore.QRect(20, 270, 181, 31))
        self.comboBox_tipoEntrada.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_tipoEntrada.setObjectName("comboBox_tipoEntrada")
        self.label_5 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 131, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_cantidad = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_cantidad.setGeometry(QtCore.QRect(320, 270, 81, 31))
        self.comboBox_cantidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_cantidad.setObjectName("comboBox_cantidad")
        self.label_6 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_6.setGeometry(QtCore.QRect(320, 250, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_fila = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_fila.setGeometry(QtCore.QRect(110, 210, 81, 31))
        self.comboBox_fila.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_fila.setObjectName("comboBox_fila")
        self.label_7 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_7.setGeometry(QtCore.QRect(110, 190, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox_butacas = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_butacas.setGeometry(QtCore.QRect(200, 210, 81, 31))
        self.comboBox_butacas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_butacas.setObjectName("comboBox_butacas")
        self.label_8 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_8.setGeometry(QtCore.QRect(200, 190, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 161, 21))
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_10.setGeometry(QtCore.QRect(10, 550, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tableWidget_tickets = QtWidgets.QTableWidget(parent=Form_Tickets)
        self.tableWidget_tickets.setGeometry(QtCore.QRect(10, 330, 631, 191))
        self.tableWidget_tickets.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_tickets.setObjectName("tableWidget_tickets")
        self.tableWidget_tickets.setColumnCount(6)
        self.tableWidget_tickets.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tickets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tickets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tickets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tickets.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tickets.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tickets.setHorizontalHeaderItem(5, item)
        self.pushButton_ingresar = QtWidgets.QPushButton(parent=Form_Tickets)
        self.pushButton_ingresar.setGeometry(QtCore.QRect(30, 580, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_ingresar.setFont(font)
        self.pushButton_ingresar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(147, 147, 0);\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ic/mas (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_ingresar.setIcon(icon)
        self.pushButton_ingresar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_ingresar.setObjectName("pushButton_ingresar")
        self.pushButton_seleccionar = QtWidgets.QPushButton(parent=Form_Tickets)
        self.pushButton_seleccionar.setGeometry(QtCore.QRect(300, 580, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_seleccionar.setFont(font)
        self.pushButton_seleccionar.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(147, 147, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ic/eliminar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_seleccionar.setIcon(icon1)
        self.pushButton_seleccionar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_seleccionar.setObjectName("pushButton_seleccionar")
        self.pushButton_imprimir = QtWidgets.QPushButton(parent=Form_Tickets)
        self.pushButton_imprimir.setGeometry(QtCore.QRect(340, 540, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton_imprimir.setFont(font)
        self.pushButton_imprimir.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ic/imprimir-contorno-del-boton.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_imprimir.setIcon(icon2)
        self.pushButton_imprimir.setObjectName("pushButton_imprimir")
        self.label_9 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_9.setGeometry(QtCore.QRect(210, 250, 81, 20))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_11.setGeometry(QtCore.QRect(210, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.comboBox_categoria = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_categoria.setGeometry(QtCore.QRect(210, 150, 241, 31))
        self.comboBox_categoria.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_categoria.setObjectName("comboBox_categoria")
        self.comboBox_nombre = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_nombre.setGeometry(QtCore.QRect(460, 150, 181, 31))
        self.comboBox_nombre.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_nombre.setObjectName("comboBox_nombre")
        self.label_12 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_12.setGeometry(QtCore.QRect(460, 130, 61, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_idTickets = QtWidgets.QLineEdit(parent=Form_Tickets)
        self.lineEdit_idTickets.setEnabled(False)
        self.lineEdit_idTickets.setGeometry(QtCore.QRect(480, 30, 161, 31))
        self.lineEdit_idTickets.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_idTickets.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_idTickets.setObjectName("lineEdit_idTickets")
        self.lineEdit_precio = QtWidgets.QLineEdit(parent=Form_Tickets)
        self.lineEdit_precio.setGeometry(QtCore.QRect(210, 270, 91, 31))
        self.lineEdit_precio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_precio.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_precio.setObjectName("lineEdit_precio")
        self.pushButton_eliminar = QtWidgets.QPushButton(parent=Form_Tickets)
        self.pushButton_eliminar.setGeometry(QtCore.QRect(470, 580, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.pushButton_eliminar.setFont(font)
        self.pushButton_eliminar.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(147, 147, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_eliminar.setIcon(icon1)
        self.pushButton_eliminar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.lineEdit__total = QtWidgets.QLineEdit(parent=Form_Tickets)
        self.lineEdit__total.setGeometry(QtCore.QRect(120, 540, 201, 31))
        self.lineEdit__total.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit__total.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit__total.setObjectName("lineEdit__total")
        self.comboBox_fecha = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_fecha.setGeometry(QtCore.QRect(20, 150, 171, 31))
        self.comboBox_fecha.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_fecha.setObjectName("comboBox_fecha")
        self.comboBox_evento = QtWidgets.QComboBox(parent=Form_Tickets)
        self.comboBox_evento.setGeometry(QtCore.QRect(20, 90, 301, 31))
        self.comboBox_evento.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_evento.setObjectName("comboBox_evento")
        self.label_13 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_13.setGeometry(QtCore.QRect(20, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton_seleccionar_2 = QtWidgets.QPushButton(parent=Form_Tickets)
        self.pushButton_seleccionar_2.setGeometry(QtCore.QRect(430, 260, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_seleccionar_2.setFont(font)
        self.pushButton_seleccionar_2.setStyleSheet("background-color: rgb(255, 135, 80);\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);")
        self.pushButton_seleccionar_2.setIcon(icon1)
        self.pushButton_seleccionar_2.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_seleccionar_2.setObjectName("pushButton_seleccionar_2")
        self.label_14 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_14.setGeometry(QtCore.QRect(20, 310, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.tableWidget_alla_tickets = QtWidgets.QTableWidget(parent=Form_Tickets)
        self.tableWidget_alla_tickets.setGeometry(QtCore.QRect(670, 30, 631, 491))
        self.tableWidget_alla_tickets.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_alla_tickets.setObjectName("tableWidget_alla_tickets")
        self.tableWidget_alla_tickets.setColumnCount(13)
        self.tableWidget_alla_tickets.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_alla_tickets.setHorizontalHeaderItem(12, item)
        self.pushButton_listarAll = QtWidgets.QPushButton(parent=Form_Tickets)
        self.pushButton_listarAll.setGeometry(QtCore.QRect(680, 580, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.pushButton_listarAll.setFont(font)
        self.pushButton_listarAll.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 85, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_listarAll.setIcon(icon1)
        self.pushButton_listarAll.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_listarAll.setObjectName("pushButton_listarAll")
        self.lineEdit_idTickets_3 = QtWidgets.QLineEdit(parent=Form_Tickets)
        self.lineEdit_idTickets_3.setEnabled(False)
        self.lineEdit_idTickets_3.setGeometry(QtCore.QRect(300, 210, 161, 31))
        self.lineEdit_idTickets_3.setStyleSheet("background-color: rgb(203, 203, 151);\n"
"border-color: rgb(203, 203, 151);\n"
"\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"\n"
"")
        self.lineEdit_idTickets_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_idTickets_3.setObjectName("lineEdit_idTickets_3")
        self.label_15 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_15.setGeometry(QtCore.QRect(300, 190, 49, 16))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=Form_Tickets)
        self.label_16.setGeometry(QtCore.QRect(300, 190, 111, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.retranslateUi(Form_Tickets)
        QtCore.QMetaObject.connectSlotsByName(Form_Tickets)


         #----------------------------------------------------------------------------------
        self.pushButton_eliminar.setEnabled(False)
        self.pushButton_seleccionar.setEnabled(False) 
        self.pushButton_imprimir.setEnabled(False)
        
        #llenar Combo Box
        #Eventos
        self.__tickets_controlles.inicializarComboBoxEventos() 
        #Lugar al tocar eventos
        self.comboBox_evento.activated.connect(lambda:self.__tickets_controlles.inicializarComboBoxEstadio())      
        #fecha 
        self.comboBox_evento.activated.connect(lambda:self.__tickets_controlles.inicializarComboBoxFechas())
        #Categoria
        self.__tickets_controlles.inicializarComboBoxCategorias()
        #Nombres
        self.comboBox_categoria.activated.connect(lambda:self.__tickets_controlles.inicializarComboBoxNombres())
        
        #sector - fila - butaca, dependen del estadio
        self.comboBox_lugar.activated.connect(lambda:self.__tickets_controlles.inicializarComboBoxSectores())
        self.comboBox_sector.activated.connect(lambda:self.__tickets_controlles.inicializarComboBoxFila())
        self.comboBox_lugar.activated.connect(lambda:self.__tickets_controlles.inicializarComboBoxButaca())

       #tipo de entrada
        self.__tickets_controlles.inicializarComboBoxTipoEntrada()
        self.comboBox_tipoEntrada.activated.connect(lambda:self.__tickets_controlles.iniciliazarPrecio())
        #cantidad
        self.__tickets_controlles.inicializarComboCantidad()

	  #-------------------------------------------------------

        self.pushButton_seleccionar_2.clicked.connect(lambda:self.__tickets_controlles.agregarGrilla(self.comboBox_tipoEntrada.currentText(), self.lineEdit_precio.text(),self.comboBox_cantidad.currentText(),self.comboBox_sector.currentText(),self.comboBox_fila.currentText(),self.comboBox_butacas.currentText()))
        
        self.pushButton_seleccionar.clicked.connect(lambda:self.__tickets_controlles.seleccionarGrilla())      

        self.pushButton_ingresar.clicked.connect(lambda:self.__tickets_controlles.ingresar(self.comboBox_lugar.currentText(),self.comboBox_fecha.currentText(),self.comboBox_categoria.currentText(),self.comboBox_nombre.currentText(),self.comboBox_sector.currentText(),self.comboBox_fila.currentText(),self.comboBox_butacas.currentText(), self.comboBox_tipoEntrada.currentText(),self.lineEdit__total.text()))

        self.__tickets_controlles.mostrarGrilla()

        self.pushButton_eliminar.clicked.connect(lambda:self.__tickets_controlles.eliminar()) 

        self.pushButton_imprimir.clicked.connect(lambda:self.__tickets_controlles.generarPDF())





    def retranslateUi(self, Form_Tickets):
        _translate = QtCore.QCoreApplication.translate
        Form_Tickets.setWindowTitle(_translate("Form_Tickets", "Tickets"))
        self.label.setText(_translate("Form_Tickets", "LUGAR:"))
        self.label_4.setText(_translate("Form_Tickets", "FECHA :"))
        self.label_3.setText(_translate("Form_Tickets", "SECTOR: "))
        self.label_5.setText(_translate("Form_Tickets", "TIPO DE ENTRADA: "))
        self.label_6.setText(_translate("Form_Tickets", "CANTIDAD:"))
        self.label_7.setText(_translate("Form_Tickets", "FILA:"))
        self.label_8.setText(_translate("Form_Tickets", "BUTACA:"))
        self.label_2.setText(_translate("Form_Tickets", "ID TICKET"))
        self.label_10.setText(_translate("Form_Tickets", "TOTAL TICKET : $ "))
        self.tableWidget_tickets.setSortingEnabled(True)
        item = self.tableWidget_tickets.horizontalHeaderItem(0)
        item.setText(_translate("Form_Tickets", "TIPO ENTRADA"))
        item = self.tableWidget_tickets.horizontalHeaderItem(1)
        item.setText(_translate("Form_Tickets", "CANTIDAD"))
        item = self.tableWidget_tickets.horizontalHeaderItem(2)
        item.setText(_translate("Form_Tickets", "PRECIO"))
        item = self.tableWidget_tickets.horizontalHeaderItem(3)
        item.setText(_translate("Form_Tickets", "SECTOR"))
        item = self.tableWidget_tickets.horizontalHeaderItem(4)
        item.setText(_translate("Form_Tickets", "FILA"))
        item = self.tableWidget_tickets.horizontalHeaderItem(5)
        item.setText(_translate("Form_Tickets", "BUTACA"))
        self.pushButton_ingresar.setText(_translate("Form_Tickets", "FINALIZAR"))
        self.pushButton_seleccionar.setText(_translate("Form_Tickets", "SELECCIONAR"))
        self.pushButton_imprimir.setText(_translate("Form_Tickets", "  IMPRIMIR"))
        self.label_9.setText(_translate("Form_Tickets", "PRECIO UN.:"))
        self.label_11.setText(_translate("Form_Tickets", "CATEGORIA:"))
        self.label_12.setText(_translate("Form_Tickets", "NOMBRE:"))
        self.pushButton_eliminar.setText(_translate("Form_Tickets", "ELIMINAR"))
        self.label_13.setText(_translate("Form_Tickets", "EVENTO"))
        self.pushButton_seleccionar_2.setText(_translate("Form_Tickets", "Agregar a la GRILLA"))
        self.label_14.setText(_translate("Form_Tickets", "GRILLA: "))
        self.tableWidget_alla_tickets.setSortingEnabled(True)
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(0)
        item.setText(_translate("Form_Tickets", "COD"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(1)
        item.setText(_translate("Form_Tickets", "DIA"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(2)
        item.setText(_translate("Form_Tickets", "SECTOR"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(3)
        item.setText(_translate("Form_Tickets", "COLOR"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(4)
        item.setText(_translate("Form_Tickets", "FILA"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(5)
        item.setText(_translate("Form_Tickets", "BUTACA"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(6)
        item.setText(_translate("Form_Tickets", "CANTIDAD"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(7)
        item.setText(_translate("Form_Tickets", "TIPO ENTRADA"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(8)
        item.setText(_translate("Form_Tickets", "$ ENTRADA"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(9)
        item.setText(_translate("Form_Tickets", "$ SECTOR"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(10)
        item.setText(_translate("Form_Tickets", "NOMBRE"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(11)
        item.setText(_translate("Form_Tickets", "LUGAR"))
        item = self.tableWidget_alla_tickets.horizontalHeaderItem(12)
        item.setText(_translate("Form_Tickets", "FESTIVAL"))
        self.pushButton_listarAll.setText(_translate("Form_Tickets", "LISTAR TODOS LOS TICKETS"))
        self.label_16.setText(_translate("Form_Tickets", "SECTOR PRECIO: "))


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Tickets = QtWidgets.QMainWindow()
        ui =  Ui_Form_Tickets()
        ui.setupUi(Tickets)      
        Tickets.show()        
        sys.exit(app.exec())