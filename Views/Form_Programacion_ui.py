import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate,QDate

from Controllers.Programaciones import Programacion_Control

class Ui_Form_Cronograma(object):
    def __init__(self):
        self.__programacion_controlles = Programacion_Control(self)

    def setupUi(self, Form_Cronograma):
        Form_Cronograma.setObjectName("Form_Cronograma")
        Form_Cronograma.resize(548, 581)
        Form_Cronograma.setMinimumSize(QtCore.QSize(548, 581))
        Form_Cronograma.setMaximumSize(QtCore.QSize(548, 581))
        Form_Cronograma.setStyleSheet("background-color: rgb(203, 203, 151);")
        self.label = QtWidgets.QLabel(parent=Form_Cronograma)
        self.label.setGeometry(QtCore.QRect(20, 30, 171, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_eventos = QtWidgets.QComboBox(parent=Form_Cronograma)
        self.comboBox_eventos.setGeometry(QtCore.QRect(20, 60, 241, 41))
        self.comboBox_eventos.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_eventos.setObjectName("comboBox_eventos")
        self.comboBox_dias = QtWidgets.QComboBox(parent=Form_Cronograma)
        self.comboBox_dias.setGeometry(QtCore.QRect(290, 60, 241, 41))
        self.comboBox_dias.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_dias.setObjectName("comboBox_dias")
        self.label_3 = QtWidgets.QLabel(parent=Form_Cronograma)
        self.label_3.setGeometry(QtCore.QRect(290, 30, 181, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_categorias = QtWidgets.QComboBox(parent=Form_Cronograma)
        self.comboBox_categorias.setGeometry(QtCore.QRect(20, 160, 241, 41))
        self.comboBox_categorias.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_categorias.setObjectName("comboBox_categorias")
        self.label_4 = QtWidgets.QLabel(parent=Form_Cronograma)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_nombres = QtWidgets.QComboBox(parent=Form_Cronograma)
        self.comboBox_nombres.setGeometry(QtCore.QRect(290, 160, 241, 41))
        self.comboBox_nombres.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_nombres.setObjectName("comboBox_nombres")
        self.label_5 = QtWidgets.QLabel(parent=Form_Cronograma)
        self.label_5.setGeometry(QtCore.QRect(290, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableWidget_cronograma = QtWidgets.QTableWidget(parent=Form_Cronograma)
        self.tableWidget_cronograma.setGeometry(QtCore.QRect(20, 290, 501, 251))
        self.tableWidget_cronograma.setStyleSheet("\n"
"border-style: solid;\n"
"\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_cronograma.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_cronograma.setObjectName("tableWidget_cronograma")
        self.tableWidget_cronograma.setColumnCount(6)
        self.tableWidget_cronograma.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cronograma.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cronograma.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cronograma.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cronograma.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cronograma.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cronograma.setHorizontalHeaderItem(5, item)
        self.pushButton_cargar = QtWidgets.QPushButton(parent=Form_Cronograma)
        self.pushButton_cargar.setGeometry(QtCore.QRect(90, 240, 75, 31))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_cargar.setFont(font)
        self.pushButton_cargar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_cargar.setObjectName("pushButton_cargar")
        self.pushButton_modificar = QtWidgets.QPushButton(parent=Form_Cronograma)
        self.pushButton_modificar.setGeometry(QtCore.QRect(180, 240, 75, 31))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_modificar.setFont(font)
        self.pushButton_modificar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_modificar.setObjectName("pushButton_modificar")
        self.pushButton_seleccionar = QtWidgets.QPushButton(parent=Form_Cronograma)
        self.pushButton_seleccionar.setGeometry(QtCore.QRect(270, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_seleccionar.setFont(font)
        self.pushButton_seleccionar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_seleccionar.setObjectName("pushButton_seleccionar")
        self.pushButton_eliminar = QtWidgets.QPushButton(parent=Form_Cronograma)
        self.pushButton_eliminar.setGeometry(QtCore.QRect(380, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_eliminar.setFont(font)
        self.pushButton_eliminar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")

        self.retranslateUi(Form_Cronograma)
        QtCore.QMetaObject.connectSlotsByName(Form_Cronograma)

#---------------------------------------------------------------------------------------
        self.pushButton_eliminar.setEnabled(False)
        self.pushButton_modificar.setEnabled(False) 
        
        self.__programacion_controlles.inicializarComboBoxEventos() 
        self.comboBox_eventos.activated.connect(lambda:self.__programacion_controlles.inicializarComboBoxFechas())      
        self.__programacion_controlles.inicializarComboBoxCategorias()
        self.comboBox_categorias.activated.connect(lambda:self.__programacion_controlles.inicializarComboBoxNombres())
        self.comboBox_nombres.activated.connect(lambda:self.__programacion_controlles.horarioDisponibleByEvento(self.comboBox_eventos.currentText(),self.comboBox_dias.currentText(),self.comboBox_categorias.currentText()))

        self.__programacion_controlles.showProgramacion()
        self.pushButton_cargar.clicked.connect(lambda:self.__programacion_controlles.cargarProgramacion(self.comboBox_eventos.currentText(),self.comboBox_dias.currentText(),self.comboBox_categorias.currentText(),self.comboBox_nombres.currentText()))
        self.pushButton_seleccionar.clicked.connect(lambda:self.__programacion_controlles.seleccionar())
        self.pushButton_modificar.clicked.connect(lambda:self.__programacion_controlles.modificar(self.comboBox_eventos.currentText(),self.comboBox_dias.currentText(),self.comboBox_categorias.currentText(),self.comboBox_nombres.currentText()))
        self.pushButton_eliminar.clicked.connect(lambda:self.__programacion_controlles.eliminar())





    def retranslateUi(self, Form_Cronograma):
        _translate = QtCore.QCoreApplication.translate
        Form_Cronograma.setWindowTitle(_translate("Form_Cronograma", "PROGRAMACION"))
        self.label.setText(_translate("Form_Cronograma", "EVENTO:"))
        self.label_3.setText(_translate("Form_Cronograma", "FECHAS DISPONIBLES:"))
        self.label_4.setText(_translate("Form_Cronograma", "CATEGORIA:"))
        self.label_5.setText(_translate("Form_Cronograma", "NOMBRE:"))
        self.tableWidget_cronograma.setSortingEnabled(True)
        item = self.tableWidget_cronograma.horizontalHeaderItem(0)
        item.setText(_translate("Form_Cronograma", "Num"))
        item = self.tableWidget_cronograma.horizontalHeaderItem(1)
        item.setText(_translate("Form_Cronograma", "EVENTO"))
        item = self.tableWidget_cronograma.horizontalHeaderItem(2)
        item.setText(_translate("Form_Cronograma", "FECHA"))
        item = self.tableWidget_cronograma.horizontalHeaderItem(3)
        item.setText(_translate("Form_Cronograma", "CATEGORIA"))
        item = self.tableWidget_cronograma.horizontalHeaderItem(4)
        item.setText(_translate("Form_Cronograma", "NOMBRE"))
        item = self.tableWidget_cronograma.horizontalHeaderItem(5)
        item.setText(_translate("Form_Cronograma", "HORA INICIO"))
        self.pushButton_cargar.setText(_translate("Form_Cronograma", "CARGAR"))
        self.pushButton_modificar.setText(_translate("Form_Cronograma", "MODIFICAR"))
        self.pushButton_seleccionar.setText(_translate("Form_Cronograma", "SELECCIONAR"))
        self.pushButton_eliminar.setText(_translate("Form_Cronograma", "ELIMINAR"))

if __name__ == "__main__":

        import sys
        app = QtWidgets.QApplication(sys.argv)
        Programacion = QtWidgets.QMainWindow()
        ui = Ui_Form_Cronograma()
        ui.setupUi(Programacion)      
        Programacion.show()
        sys.exit(app.exec())
