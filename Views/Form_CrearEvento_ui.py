import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)



from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate,QDate

from Controllers.Eventos import Evento_Control


class Ui_Form_crearEvento(object):
    def __init__(self):
        self.__crearEvento_controlles = Evento_Control(self)   
    def setupUi(self, Form_crearEvento):
        Form_crearEvento.setObjectName("Form_crearEvento")
        Form_crearEvento.resize(650, 510)
        Form_crearEvento.setMinimumSize(QtCore.QSize(650, 510))
        Form_crearEvento.setMaximumSize(QtCore.QSize(650, 510))
        Form_crearEvento.setStyleSheet("background-color: rgb(203, 203, 151);")
        self.label = QtWidgets.QLabel(parent=Form_crearEvento)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=Form_crearEvento)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form_crearEvento)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 191, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form_crearEvento)
        self.label_5.setGeometry(QtCore.QRect(270, 180, 191, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableWidget_crearEvento = QtWidgets.QTableWidget(parent=Form_crearEvento)
        self.tableWidget_crearEvento.setGeometry(QtCore.QRect(10, 310, 621, 192))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.tableWidget_crearEvento.setFont(font)
        self.tableWidget_crearEvento.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_crearEvento.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_crearEvento.setObjectName("tableWidget_crearEvento")
        self.tableWidget_crearEvento.setColumnCount(6)
        self.tableWidget_crearEvento.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_crearEvento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_crearEvento.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_crearEvento.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_crearEvento.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_crearEvento.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_crearEvento.setHorizontalHeaderItem(5, item)
        self.tableWidget_crearEvento.verticalHeader().setDefaultSectionSize(100)
        self.tableWidget_crearEvento.verticalHeader().setMinimumSectionSize(32)
        self.pushButton_modificar = QtWidgets.QPushButton(parent=Form_crearEvento)
        self.pushButton_modificar.setEnabled(False)
        self.pushButton_modificar.setGeometry(QtCore.QRect(290, 260, 101, 24))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_modificar.setFont(font)
        self.pushButton_modificar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_modificar.setObjectName("pushButton_modificar")
        self.pushButton_seleccionar = QtWidgets.QPushButton(parent=Form_crearEvento)
        self.pushButton_seleccionar.setEnabled(False)
        self.pushButton_seleccionar.setGeometry(QtCore.QRect(160, 260, 101, 24))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_seleccionar.setFont(font)
        self.pushButton_seleccionar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_seleccionar.setObjectName("pushButton_seleccionar")
        self.pushButton_cargar = QtWidgets.QPushButton(parent=Form_crearEvento)
        self.pushButton_cargar.setGeometry(QtCore.QRect(30, 260, 101, 24))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        self.pushButton_cargar.setFont(font)
        self.pushButton_cargar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_cargar.setObjectName("pushButton_cargar")
        self.pushButton_eliminar = QtWidgets.QPushButton(parent=Form_crearEvento)
        self.pushButton_eliminar.setEnabled(False)
        self.pushButton_eliminar.setGeometry(QtCore.QRect(410, 260, 101, 24))
        font = QtGui.QFont()
        font.setFamily("FONTSPRING DEMO - Organetto Light")
        self.pushButton_eliminar.setFont(font)
        self.pushButton_eliminar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.comboBox_estadios = QtWidgets.QComboBox(parent=Form_crearEvento)
        self.comboBox_estadios.setEnabled(True)
        self.comboBox_estadios.setGeometry(QtCore.QRect(20, 120, 201, 31))
        self.comboBox_estadios.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.comboBox_estadios.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_estadios.setObjectName("comboBox_estadios")
        self.label_6 = QtWidgets.QLabel(parent=Form_crearEvento)
        self.label_6.setGeometry(QtCore.QRect(270, 100, 111, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_categoria = QtWidgets.QComboBox(parent=Form_crearEvento)
        self.comboBox_categoria.setEnabled(True)
        self.comboBox_categoria.setGeometry(QtCore.QRect(270, 120, 201, 31))
        self.comboBox_categoria.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.comboBox_categoria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_categoria.setObjectName("comboBox_categoria")
        self.lineEdit_nombre = QtWidgets.QLineEdit(parent=Form_crearEvento)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(20, 50, 451, 41))
        self.lineEdit_nombre.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_nombre.setMaxLength(45)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.dateEdit_inicio = QtWidgets.QDateEdit(parent=Form_crearEvento)
        self.dateEdit_inicio.setEnabled(False)
        self.dateEdit_inicio.setGeometry(QtCore.QRect(10, 200, 110, 22))
        self.dateEdit_inicio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.dateEdit_inicio.setCalendarPopup(True)
        self.dateEdit_inicio.setObjectName("dateEdit_inicio")
        self.timeEdit_inicio = QtWidgets.QTimeEdit(parent=Form_crearEvento)
        self.timeEdit_inicio.setEnabled(False)
        self.timeEdit_inicio.setGeometry(QtCore.QRect(130, 200, 118, 22))
        self.timeEdit_inicio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit_inicio.setCalendarPopup(True)
        self.timeEdit_inicio.setObjectName("timeEdit_inicio")
        self.dateEdit_fin = QtWidgets.QDateEdit(parent=Form_crearEvento)
        self.dateEdit_fin.setEnabled(False)
        self.dateEdit_fin.setGeometry(QtCore.QRect(270, 200, 110, 22))
        self.dateEdit_fin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_fin.setCalendarPopup(True)
        self.dateEdit_fin.setObjectName("dateEdit_fin")
        self.label_7 = QtWidgets.QLabel(parent=Form_crearEvento)
        self.label_7.setGeometry(QtCore.QRect(480, 60, 161, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.dateEdit_inicio.setDate(QDate.currentDate()) # te seleccione la fecha del dia de how
        self.dateEdit_inicio.setDisplayFormat("yyyy/MM/dd") #mysql no tire error
        self.dateEdit_inicio.setMinimumDate(QDate.currentDate())  # fecha minima dia actual

        self.dateEdit_fin.setDate(QDate.currentDate()) # te seleccione la fecha del dia de how
        self.dateEdit_fin.setDisplayFormat("yyyy/MM/dd") #mysql no tire error
        self.dateEdit_fin.setMinimumDate(QDate.currentDate())  # fecha minima dia actual

        self.retranslateUi(Form_crearEvento)
        QtCore.QMetaObject.connectSlotsByName(Form_crearEvento)

        
 #-------------------------------------------------------------
        self.pushButton_eliminar.setEnabled(False)
        self.pushButton_modificar.setEnabled(False)
        
        self.__crearEvento_controlles.inicializar_comboBoxEstadios()
        self.__crearEvento_controlles.inicializar_comboBoxCategorias()
        self.__crearEvento_controlles.mostrarEventos()


        self.lineEdit_nombre.returnPressed.connect(lambda:self.__crearEvento_controlles.verificarCadenas())
        
        self.cargar = self.pushButton_cargar.clicked.connect(lambda:self.__crearEvento_controlles.cargar(self.lineEdit_nombre.text(),self.comboBox_estadios.currentText(),self.comboBox_categoria.currentText(),self.dateEdit_inicio,self.dateEdit_fin,self.timeEdit_inicio.text()))
        self.seleccionar = self.pushButton_seleccionar.clicked.connect(lambda:self.__crearEvento_controlles.seleccionar())
        self.modificar = self.pushButton_modificar.clicked.connect(lambda:self.__crearEvento_controlles.modificar(self.lineEdit_nombre.text(),self.comboBox_estadios.currentText(),self.comboBox_categoria.currentText(),self.dateEdit_inicio.text(),self.timeEdit_inicio.text(),self.dateEdit_fin.text()))
        self.eliminar = self.pushButton_eliminar.clicked.connect(lambda:self.__crearEvento_controlles.eliminar(self.lineEdit_nombre.text(),self.comboBox_estadios.currentText()))
 
        
        Form_crearEvento.setTabOrder(self.lineEdit_nombre, self.comboBox_estadios)
        Form_crearEvento.setTabOrder(self.comboBox_estadios, self.comboBox_categoria)
        Form_crearEvento.setTabOrder(self.comboBox_categoria, self.pushButton_cargar)
        Form_crearEvento.setTabOrder(self.pushButton_cargar, self.pushButton_seleccionar)
        Form_crearEvento.setTabOrder(self.pushButton_seleccionar, self.pushButton_modificar)
        Form_crearEvento.setTabOrder(self.pushButton_modificar, self.pushButton_eliminar)
        Form_crearEvento.setTabOrder(self.pushButton_eliminar, self.tableWidget_crearEvento)

    def retranslateUi(self, Form_crearEvento):
        _translate = QtCore.QCoreApplication.translate
        Form_crearEvento.setWindowTitle(_translate("Form_crearEvento", "Crear Evento"))
        self.label.setText(_translate("Form_crearEvento", "NOMBRE:"))
        self.label_3.setText(_translate("Form_crearEvento", "LUGAR:"))
        self.label_4.setText(_translate("Form_crearEvento", "FECHA Y HORARIO DE INICIO:"))
        self.label_5.setText(_translate("Form_crearEvento", " FECHA DE FINALIZACION :"))
        self.tableWidget_crearEvento.setSortingEnabled(True)
        item = self.tableWidget_crearEvento.horizontalHeaderItem(0)
        item.setText(_translate("Form_crearEvento", "NOMBRE"))
        item = self.tableWidget_crearEvento.horizontalHeaderItem(1)
        item.setText(_translate("Form_crearEvento", "LUGAR"))
        item = self.tableWidget_crearEvento.horizontalHeaderItem(2)
        item.setText(_translate("Form_crearEvento", "CATEGORIA"))
        item = self.tableWidget_crearEvento.horizontalHeaderItem(3)
        item.setText(_translate("Form_crearEvento", "DESDE"))
        item = self.tableWidget_crearEvento.horizontalHeaderItem(4)
        item.setText(_translate("Form_crearEvento", "HS."))
        item = self.tableWidget_crearEvento.horizontalHeaderItem(5)
        item.setText(_translate("Form_crearEvento", "HASTA"))
        self.pushButton_modificar.setText(_translate("Form_crearEvento", "MODIFICAR"))
        self.pushButton_seleccionar.setText(_translate("Form_crearEvento", "SELECCIONAR "))
        self.pushButton_cargar.setText(_translate("Form_crearEvento", "CARGAR"))
        self.pushButton_eliminar.setText(_translate("Form_crearEvento", "ELIMINAR"))
        self.label_6.setText(_translate("Form_crearEvento", "Categorias:"))
        self.dateEdit_inicio.setDisplayFormat(_translate("Form_crearEvento", "yyyy/MM/dd"))
        self.dateEdit_fin.setDisplayFormat(_translate("Form_crearEvento", "yyyy/MM/dd"))
        self.label_7.setText(_translate("Form_crearEvento", "Presione ENTER, para cambiar"))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        CrearEvento = QtWidgets.QMainWindow()
        ui = Ui_Form_crearEvento()
        ui.setupUi(CrearEvento)      
        CrearEvento.show()
        sys.exit(app.exec())