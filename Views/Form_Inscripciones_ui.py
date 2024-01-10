import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate,QDate

from Controllers.Inscripciones import Inscripciones_Control

class Ui_Form_Inscripciones(object):
    
    def __init__(self):
        self.__inscripciones_controlles = Inscripciones_Control(self)
        
    def setupUi(self, Form_Inscripciones):
        Form_Inscripciones.setObjectName("Form_Inscripciones")
        Form_Inscripciones.resize(526, 510)
        Form_Inscripciones.setMinimumSize(QtCore.QSize(526, 510))
        Form_Inscripciones.setMaximumSize(QtCore.QSize(526, 510))
        font = QtGui.QFont()
        font.setFamily("Arial")
        Form_Inscripciones.setFont(font)
        Form_Inscripciones.setStyleSheet("background-color: rgb(203, 203, 151);")
        self.pushButton_cargar = QtWidgets.QPushButton(parent=Form_Inscripciones)
        self.pushButton_cargar.setEnabled(False)
        self.pushButton_cargar.setGeometry(QtCore.QRect(30, 270, 101, 24))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        self.pushButton_cargar.setFont(font)
        self.pushButton_cargar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_cargar.setObjectName("pushButton_cargar")
        self.tableWidget_inscripciones = QtWidgets.QTableWidget(parent=Form_Inscripciones)
        self.tableWidget_inscripciones.setGeometry(QtCore.QRect(10, 310, 501, 192))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tableWidget_inscripciones.setFont(font)
        self.tableWidget_inscripciones.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_inscripciones.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_inscripciones.setObjectName("tableWidget_inscripciones")
        self.tableWidget_inscripciones.setColumnCount(4)
        self.tableWidget_inscripciones.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_inscripciones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_inscripciones.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_inscripciones.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_inscripciones.setHorizontalHeaderItem(3, item)
        self.tableWidget_inscripciones.verticalHeader().setDefaultSectionSize(100)
        self.tableWidget_inscripciones.verticalHeader().setMinimumSectionSize(32)
        self.pushButton_modificar = QtWidgets.QPushButton(parent=Form_Inscripciones)
        self.pushButton_modificar.setEnabled(False)
        self.pushButton_modificar.setGeometry(QtCore.QRect(290, 270, 101, 24))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_modificar.setFont(font)
        self.pushButton_modificar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_modificar.setObjectName("pushButton_modificar")
        self.pushButton_eliminar = QtWidgets.QPushButton(parent=Form_Inscripciones)
        self.pushButton_eliminar.setEnabled(False)
        self.pushButton_eliminar.setGeometry(QtCore.QRect(410, 270, 101, 24))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_eliminar.setFont(font)
        self.pushButton_eliminar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.label_3 = QtWidgets.QLabel(parent=Form_Inscripciones)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(parent=Form_Inscripciones)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_seleccionar = QtWidgets.QPushButton(parent=Form_Inscripciones)
        self.pushButton_seleccionar.setEnabled(False)
        self.pushButton_seleccionar.setGeometry(QtCore.QRect(160, 270, 101, 24))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_seleccionar.setFont(font)
        self.pushButton_seleccionar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_seleccionar.setObjectName("pushButton_seleccionar")
        self.comboBox_categoria = QtWidgets.QComboBox(parent=Form_Inscripciones)
        self.comboBox_categoria.setGeometry(QtCore.QRect(20, 50, 241, 41))
        self.comboBox_categoria.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_categoria.setObjectName("comboBox_categoria")
        self.label_4 = QtWidgets.QLabel(parent=Form_Inscripciones)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 161, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form_Inscripciones)
        self.label_5.setGeometry(QtCore.QRect(280, 110, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_nombre = QtWidgets.QLineEdit(parent=Form_Inscripciones)
        self.lineEdit_nombre.setEnabled(True)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(20, 130, 241, 41))
        self.lineEdit_nombre.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_nombre.setMaxLength(45)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_correo = QtWidgets.QLineEdit(parent=Form_Inscripciones)
        self.lineEdit_correo.setEnabled(False)
        self.lineEdit_correo.setGeometry(QtCore.QRect(270, 130, 241, 41))
        self.lineEdit_correo.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_correo.setMaxLength(45)
        self.lineEdit_correo.setObjectName("lineEdit_correo")
        self.lineEdit_detalle = QtWidgets.QLineEdit(parent=Form_Inscripciones)
        self.lineEdit_detalle.setEnabled(False)
        self.lineEdit_detalle.setGeometry(QtCore.QRect(20, 210, 491, 51))
        self.lineEdit_detalle.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_detalle.setMaxLength(95)
        self.lineEdit_detalle.setObjectName("lineEdit_detalle")
        self.label_2 = QtWidgets.QLabel(parent=Form_Inscripciones)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form_Inscripciones)
        QtCore.QMetaObject.connectSlotsByName(Form_Inscripciones)

#-------------------------------------------------------------------------------------------------
        self.__inscripciones_controlles.inicializar_comboBoxCategorias()
        self.__inscripciones_controlles.mostrarInscriptos()

        self.lineEdit_nombre.returnPressed.connect(self.__inscripciones_controlles.verificarCadenas)
        self.lineEdit_correo.returnPressed.connect(self.__inscripciones_controlles.verificarNumCaracter)

        self.cargar = self.pushButton_cargar.clicked.connect(lambda:self.__inscripciones_controlles.cargar(self.comboBox_categoria.currentText(),self.lineEdit_nombre.text(),self.lineEdit_detalle.text(),self.lineEdit_correo.text()))
        self.seleccionar = self.pushButton_seleccionar.clicked.connect(lambda:self.__inscripciones_controlles.seleccionar())
        self.modificar = self.pushButton_modificar.clicked.connect(lambda:self.__inscripciones_controlles.modificar(self.comboBox_categoria.currentText(),self.lineEdit_nombre.text(),self.lineEdit_detalle.text(),self.lineEdit_correo.text()))
        self.eliminar = self.pushButton_eliminar.clicked.connect(lambda:self.__inscripciones_controlles.eliminar(self.lineEdit_nombre.text()))


    def retranslateUi(self, Form_Inscripciones):
        _translate = QtCore.QCoreApplication.translate
        Form_Inscripciones.setWindowTitle(_translate("Form_Inscripciones", "INSCRIPCIONES"))
        self.pushButton_cargar.setText(_translate("Form_Inscripciones", "CARGAR"))
        self.tableWidget_inscripciones.setSortingEnabled(True)
        item = self.tableWidget_inscripciones.horizontalHeaderItem(0)
        item.setText(_translate("Form_Inscripciones", "NOMBRE"))
        item = self.tableWidget_inscripciones.horizontalHeaderItem(1)
        item.setText(_translate("Form_Inscripciones", "CORREO"))
        item = self.tableWidget_inscripciones.horizontalHeaderItem(2)
        item.setText(_translate("Form_Inscripciones", "COMENTARIO"))
        item = self.tableWidget_inscripciones.horizontalHeaderItem(3)
        item.setText(_translate("Form_Inscripciones", "CATEGORIA"))
        self.pushButton_modificar.setText(_translate("Form_Inscripciones", "MODIFICAR"))
        self.pushButton_eliminar.setText(_translate("Form_Inscripciones", "ELIMINAR"))
        self.label_3.setText(_translate("Form_Inscripciones", "NOMBRE:"))
        self.label.setText(_translate("Form_Inscripciones", "CATEGORIA:"))
        self.pushButton_seleccionar.setText(_translate("Form_Inscripciones", "SELECCIONAR "))
        self.label_4.setText(_translate("Form_Inscripciones", "COMENTARIO:"))
        self.label_5.setText(_translate("Form_Inscripciones", "CORREO:"))
        self.label_2.setText(_translate("Form_Inscripciones", "Presiones ENTER, para ingresar dato"))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Inscripciones = QtWidgets.QMainWindow()
        ui = Ui_Form_Inscripciones()
        ui.setupUi(Inscripciones)      
        Inscripciones.show()
        sys.exit(app.exec())