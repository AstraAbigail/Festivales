import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt6 import QtCore, QtGui, QtWidgets

from Views.Form_CrearEvento_ui import Ui_Form_crearEvento 
from Views.Form_Inscripciones_ui import Ui_Form_Inscripciones 
from Views.Form_Programacion_ui import Ui_Form_Cronograma
from Views.Form_Tickets_ui import Ui_Form_Tickets 
from Views.main_configuracion_ui import Ui_MainWindow_configuracion 

from Controllers.Eventos import Evento_Control
from Controllers.Inscripciones import Inscripciones_Control
from Controllers.Programaciones import Programacion_Control
from Controllers.Tickets import Ticket_Control
from Controllers.MenuPrincipal import MenuPrincipal_Control



class Ui_MainWindow(object):
     
    def __init__(self):
        self.__crearEvento_controlles = Evento_Control(self)
        self.__inscripciones_controlles = Inscripciones_Control(self)
        self.__programaciones_controlles = Programacion_Control(self)
        self.__tickets_controlles = Ticket_Control(self)
        self.__menuPrincipal_controlls =  MenuPrincipal_Control(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 343)
        MainWindow.setMinimumSize(QtCore.QSize(734, 343))
        MainWindow.setMaximumSize(QtCore.QSize(734, 343))
        MainWindow.setStyleSheet("background-color: rgb(203, 203, 151);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_crearEvento = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_crearEvento.setGeometry(QtCore.QRect(40, 50, 151, 151))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(13)
        self.pushButton_crearEvento.setFont(font)
        self.pushButton_crearEvento.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"hover: {\n"
"    background-color:#54d777;\n"
"}")
        self.pushButton_crearEvento.setObjectName("pushButton_crearEvento")
        self.pushButton_inscripciones = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_inscripciones.setGeometry(QtCore.QRect(210, 50, 151, 151))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        font.setPointSize(13)
        self.pushButton_inscripciones.setFont(font)
        self.pushButton_inscripciones.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_inscripciones.setObjectName("pushButton_inscripciones")
        self.pushButton_cronograma = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_cronograma.setGeometry(QtCore.QRect(380, 50, 151, 151))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(13)
        self.pushButton_cronograma.setFont(font)
        self.pushButton_cronograma.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_cronograma.setObjectName("pushButton_cronograma")
        self.pushButton_tickets = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_tickets.setGeometry(QtCore.QRect(550, 50, 151, 151))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(13)
        self.pushButton_tickets.setFont(font)
        self.pushButton_tickets.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_tickets.setObjectName("pushButton_tickets")
        self.pushButton_configuracion = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_configuracion.setGeometry(QtCore.QRect(40, 220, 661, 71))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(13)
        self.pushButton_configuracion.setFont(font)
        self.pushButton_configuracion.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_configuracion.setObjectName("pushButton_configuracion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
        #Eventos---------------------------------------------
        
        self.crearEvento  = self.pushButton_crearEvento.clicked.connect(lambda:self.__crearEvento_controlles.showWindowEvento(Ui_Form_crearEvento))
        self.inscripciones = self.pushButton_inscripciones.clicked.connect(lambda:self.__inscripciones_controlles.showWindowInscripciones(Ui_Form_Inscripciones ))
        self.tickets = self.pushButton_tickets.clicked.connect(lambda:self.__tickets_controlles.showWindowTicket(Ui_Form_Tickets))
        self.configuracion = self.pushButton_configuracion.clicked.connect(lambda:self.__menuPrincipal_controlls.showWindowConfiguracion(Ui_MainWindow_configuracion ))      
        self.programacion = self.pushButton_cronograma.clicked.connect(lambda:self.__programaciones_controlles.showWindowProgramaciones(Ui_Form_Cronograma))

        #----------------------------------------------------


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Principal"))
        self.pushButton_crearEvento.setText(_translate("MainWindow", "CREAR EVENTO"))
        self.pushButton_inscripciones.setText(_translate("MainWindow", "INSCRIPCIONES"))
        self.pushButton_cronograma.setText(_translate("MainWindow", "CRONOGRAMA"))
        self.pushButton_tickets.setText(_translate("MainWindow", "TICKETS"))
        self.pushButton_configuracion.setText(_translate("MainWindow", "CONFIGURACION"))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        menuPrincipal = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(menuPrincipal)      
        menuPrincipal.show()
        sys.exit(app.exec())