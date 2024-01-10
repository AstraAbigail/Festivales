
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)



from Controllers.Categorias import Categorias_Control
from Controllers.Estadios import Estadio_Control
from Controllers.Tarifas import Tarifas_Control
from Controllers.Sectores import Sector_Control




from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Ui_MainWindow_configuracion(object):
    def __init__(self):
        self.__tarifa_controlles = Tarifas_Control(self)
        self.__categorias_controlles = Categorias_Control(self)
        self.__estadios_controlles = Estadio_Control(self)
        self.__sectores_controlles = Sector_Control(self)
    def setupUi(self, MainWindow_configuracion):
        MainWindow_configuracion.setObjectName("MainWindow_configuracion")
        MainWindow_configuracion.resize(748, 746)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_configuracion)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_Categorias = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget_Categorias.setGeometry(QtCore.QRect(0, 0, 743, 718))
        self.tabWidget_Categorias.setMinimumSize(QtCore.QSize(743, 718))
        self.tabWidget_Categorias.setMaximumSize(QtCore.QSize(743, 718))
        self.tabWidget_Categorias.setSizeIncrement(QtCore.QSize(743, 0))
        self.tabWidget_Categorias.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.tabWidget_Categorias.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.tabWidget_Categorias.setObjectName("tabWidget_Categorias")
        self.Categorias = QtWidgets.QWidget()
        self.Categorias.setObjectName("Categorias")
        self.tableWidget_categorias = QtWidgets.QTableWidget(parent=self.Categorias)
        self.tableWidget_categorias.setGeometry(QtCore.QRect(70, 290, 581, 251))
        self.tableWidget_categorias.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_categorias.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_categorias.setObjectName("tableWidget_categorias")
        self.tableWidget_categorias.setColumnCount(1)
        self.tableWidget_categorias.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_categorias.setHorizontalHeaderItem(0, item)
        self.label_2 = QtWidgets.QLabel(parent=self.Categorias)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 171, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_categorias = QtWidgets.QLineEdit(parent=self.Categorias)
        self.lineEdit_categorias.setGeometry(QtCore.QRect(70, 150, 361, 41))
        self.lineEdit_categorias.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_categorias.setObjectName("lineEdit_categorias")
        self.pushButton_Cat_Ingresar = QtWidgets.QPushButton(parent=self.Categorias)
        self.pushButton_Cat_Ingresar.setGeometry(QtCore.QRect(70, 220, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_Cat_Ingresar.setFont(font)
        self.pushButton_Cat_Ingresar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(171, 184, 89);\n"
"\n"
"")
        self.pushButton_Cat_Ingresar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Cat_Ingresar.setObjectName("pushButton_Cat_Ingresar")
        self.pushButton_Cat_Seleccionar = QtWidgets.QPushButton(parent=self.Categorias)
        self.pushButton_Cat_Seleccionar.setGeometry(QtCore.QRect(180, 220, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_Cat_Seleccionar.setFont(font)
        self.pushButton_Cat_Seleccionar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(171, 184, 89);")
        self.pushButton_Cat_Seleccionar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Cat_Seleccionar.setObjectName("pushButton_Cat_Seleccionar")
        self.pushButton_Cat_Editar = QtWidgets.QPushButton(parent=self.Categorias)
        self.pushButton_Cat_Editar.setGeometry(QtCore.QRect(300, 220, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_Cat_Editar.setFont(font)
        self.pushButton_Cat_Editar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(171, 184, 89);")
        self.pushButton_Cat_Editar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Cat_Editar.setObjectName("pushButton_Cat_Editar")
        self.pushButton_Cat_Eliminar = QtWidgets.QPushButton(parent=self.Categorias)
        self.pushButton_Cat_Eliminar.setGeometry(QtCore.QRect(410, 220, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_Cat_Eliminar.setFont(font)
        self.pushButton_Cat_Eliminar.setStyleSheet("background-color: rgb(171, 184, 89);\n"
"\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);")
        self.pushButton_Cat_Eliminar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Cat_Eliminar.setCheckable(False)
        self.pushButton_Cat_Eliminar.setObjectName("pushButton_Cat_Eliminar")
        self.label_26 = QtWidgets.QLabel(parent=self.Categorias)
        self.label_26.setGeometry(QtCore.QRect(70, 120, 141, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.tabWidget_Categorias.addTab(self.Categorias, "")
        self.Tarifas = QtWidgets.QWidget()
        self.Tarifas.setObjectName("Tarifas")
        self.label_3 = QtWidgets.QLabel(parent=self.Tarifas)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(parent=self.Tarifas)
        self.label.setGeometry(QtCore.QRect(60, 70, 171, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget_tarifas = QtWidgets.QTableWidget(parent=self.Tarifas)
        self.tableWidget_tarifas.setGeometry(QtCore.QRect(60, 290, 371, 251))
        self.tableWidget_tarifas.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_tarifas.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_tarifas.setObjectName("tableWidget_tarifas")
        self.tableWidget_tarifas.setColumnCount(2)
        self.tableWidget_tarifas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tarifas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tarifas.setHorizontalHeaderItem(1, item)
        self.lineEdit_tipoEntrada = QtWidgets.QLineEdit(parent=self.Tarifas)
        self.lineEdit_tipoEntrada.setGeometry(QtCore.QRect(60, 120, 371, 41))
        self.lineEdit_tipoEntrada.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_tipoEntrada.setObjectName("lineEdit_tipoEntrada")
        self.lineEdit_precio = QtWidgets.QLineEdit(parent=self.Tarifas)
        self.lineEdit_precio.setGeometry(QtCore.QRect(60, 230, 371, 41))
        self.lineEdit_precio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_precio.setObjectName("lineEdit_precio")
        self.pushButton_Tar_Ingresar = QtWidgets.QPushButton(parent=self.Tarifas)
        self.pushButton_Tar_Ingresar.setGeometry(QtCore.QRect(460, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_Tar_Ingresar.setFont(font)
        self.pushButton_Tar_Ingresar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(171, 184, 89);\n"
"\n"
"")
        self.pushButton_Tar_Ingresar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Tar_Ingresar.setObjectName("pushButton_Tar_Ingresar")
        self.pushButton_Tab_Eliminar = QtWidgets.QPushButton(parent=self.Tarifas)
        self.pushButton_Tab_Eliminar.setGeometry(QtCore.QRect(580, 250, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_Tab_Eliminar.setFont(font)
        self.pushButton_Tab_Eliminar.setStyleSheet("background-color: rgb(171, 184, 89);\n"
"\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);")
        self.pushButton_Tab_Eliminar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Tab_Eliminar.setCheckable(False)
        self.pushButton_Tab_Eliminar.setObjectName("pushButton_Tab_Eliminar")
        self.pushButton_Tar_Editar = QtWidgets.QPushButton(parent=self.Tarifas)
        self.pushButton_Tar_Editar.setGeometry(QtCore.QRect(460, 250, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_Tar_Editar.setFont(font)
        self.pushButton_Tar_Editar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(171, 184, 89);")
        self.pushButton_Tar_Editar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Tar_Editar.setObjectName("pushButton_Tar_Editar")
        self.pushButton_Tar_Seleccionar = QtWidgets.QPushButton(parent=self.Tarifas)
        self.pushButton_Tar_Seleccionar.setGeometry(QtCore.QRect(580, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_Tar_Seleccionar.setFont(font)
        self.pushButton_Tar_Seleccionar.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(171, 184, 89);")
        self.pushButton_Tar_Seleccionar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Tar_Seleccionar.setObjectName("pushButton_Tar_Seleccionar")
        self.label_24 = QtWidgets.QLabel(parent=self.Tarifas)
        self.label_24.setGeometry(QtCore.QRect(60, 90, 141, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.Tarifas)
        self.label_25.setGeometry(QtCore.QRect(60, 200, 211, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.tabWidget_Categorias.addTab(self.Tarifas, "")
        self.Estadio = QtWidgets.QWidget()
        self.Estadio.setObjectName("Estadio")
        self.label_12 = QtWidgets.QLabel(parent=self.Estadio)
        self.label_12.setGeometry(QtCore.QRect(10, 190, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.tableWidget_estadio = QtWidgets.QTableWidget(parent=self.Estadio)
        self.tableWidget_estadio.setGeometry(QtCore.QRect(20, 500, 501, 181))
        self.tableWidget_estadio.setStyleSheet("border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_estadio.setObjectName("tableWidget_estadio")
        self.tableWidget_estadio.setColumnCount(5)
        self.tableWidget_estadio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_estadio.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_estadio.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_estadio.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_estadio.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_estadio.setHorizontalHeaderItem(4, item)
        self.label_7 = QtWidgets.QLabel(parent=self.Estadio)
        self.label_7.setGeometry(QtCore.QRect(10, 280, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Linotte-Light")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.Estadio)
        self.label_8.setGeometry(QtCore.QRect(270, 280, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Linotte-Light")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(parent=self.Estadio)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.Estadio)
        self.label_5.setGeometry(QtCore.QRect(390, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_verificar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_verificar.setGeometry(QtCore.QRect(260, 220, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_verificar.setFont(font)
        self.pushButton_verificar.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 203, 203);\n"
"")
        self.pushButton_verificar.setObjectName("pushButton_verificar")
        self.pushButton_confirmar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_confirmar.setGeometry(QtCore.QRect(540, 270, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_confirmar.setFont(font)
        self.pushButton_confirmar.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 203, 203);\n"
"")
        self.pushButton_confirmar.setObjectName("pushButton_confirmar")
        self.pushButton_estadioIngresar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_estadioIngresar.setEnabled(True)
        self.pushButton_estadioIngresar.setGeometry(QtCore.QRect(30, 130, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_estadioIngresar.setFont(font)
        self.pushButton_estadioIngresar.setStyleSheet("\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 203, 203);")
        self.pushButton_estadioIngresar.setObjectName("pushButton_estadioIngresar")
        self.label_6 = QtWidgets.QLabel(parent=self.Estadio)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(parent=self.Estadio)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 101, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.Estadio)
        self.label_10.setGeometry(QtCore.QRect(10, 230, 141, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.frame_datosSector = QtWidgets.QFrame(parent=self.Estadio)
        self.frame_datosSector.setGeometry(QtCore.QRect(10, 330, 741, 121))
        self.frame_datosSector.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_datosSector.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_datosSector.setObjectName("frame_datosSector")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_datosSector)
        self.label_11.setGeometry(QtCore.QRect(410, 30, 71, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_datosSector)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 141, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_datosSector)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 141, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_nombreSector = QtWidgets.QLineEdit(parent=self.frame_datosSector)
        self.lineEdit_nombreSector.setGeometry(QtCore.QRect(150, 20, 251, 31))
        self.lineEdit_nombreSector.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_nombreSector.setMaxLength(10)
        self.lineEdit_nombreSector.setObjectName("lineEdit_nombreSector")
        self.lineEdit_precioSector = QtWidgets.QLineEdit(parent=self.frame_datosSector)
        self.lineEdit_precioSector.setGeometry(QtCore.QRect(150, 60, 251, 31))
        self.lineEdit_precioSector.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_precioSector.setMaxLength(10)
        self.lineEdit_precioSector.setObjectName("lineEdit_precioSector")
        self.lineEdit_color = QtWidgets.QLineEdit(parent=self.frame_datosSector)
        self.lineEdit_color.setGeometry(QtCore.QRect(470, 20, 251, 31))
        self.lineEdit_color.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_color.setMaxLength(15)
        self.lineEdit_color.setObjectName("lineEdit_color")
        self.label_15 = QtWidgets.QLabel(parent=self.Estadio)
        self.label_15.setGeometry(QtCore.QRect(390, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("FSP DEMO - Organetto Light")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_nombre = QtWidgets.QLineEdit(parent=self.Estadio)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(110, 10, 251, 31))
        self.lineEdit_nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_nombre.setMaxLength(49)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_direccion = QtWidgets.QLineEdit(parent=self.Estadio)
        self.lineEdit_direccion.setGeometry(QtCore.QRect(480, 10, 251, 31))
        self.lineEdit_direccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_direccion.setMaxLength(49)
        self.lineEdit_direccion.setObjectName("lineEdit_direccion")
        self.lineEdit_correo = QtWidgets.QLineEdit(parent=self.Estadio)
        self.lineEdit_correo.setGeometry(QtCore.QRect(480, 50, 251, 31))
        self.lineEdit_correo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_correo.setMaxLength(49)
        self.lineEdit_correo.setObjectName("lineEdit_correo")
        self.lineEdit_telefono = QtWidgets.QLineEdit(parent=self.Estadio)
        self.lineEdit_telefono.setGeometry(QtCore.QRect(110, 50, 251, 31))
        self.lineEdit_telefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_telefono.setMaxLength(17)
        self.lineEdit_telefono.setObjectName("lineEdit_telefono")
        self.lineEdit_capTotal = QtWidgets.QLineEdit(parent=self.Estadio)
        self.lineEdit_capTotal.setGeometry(QtCore.QRect(110, 90, 251, 31))
        self.lineEdit_capTotal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_capTotal.setMaxLength(9)
        self.lineEdit_capTotal.setObjectName("lineEdit_capTotal")
        self.lineEdit_cantSectores = QtWidgets.QLineEdit(parent=self.Estadio)
        self.lineEdit_cantSectores.setGeometry(QtCore.QRect(150, 220, 101, 31))
        self.lineEdit_cantSectores.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cantSectores.setMaxLength(9)
        self.lineEdit_cantSectores.setObjectName("lineEdit_cantSectores")
        self.lineEdit_cantButacas = QtWidgets.QLineEdit(parent=self.Estadio)
        self.lineEdit_cantButacas.setGeometry(QtCore.QRect(380, 270, 101, 31))
        self.lineEdit_cantButacas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cantButacas.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_cantButacas.setObjectName("lineEdit_cantButacas")
        self.lineEdit_cantFilas = QtWidgets.QLineEdit(parent=self.Estadio)
        self.lineEdit_cantFilas.setGeometry(QtCore.QRect(100, 270, 101, 31))
        self.lineEdit_cantFilas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cantFilas.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_cantFilas.setObjectName("lineEdit_cantFilas")
        self.pushButton_Est_Seleccionar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_Est_Seleccionar.setGeometry(QtCore.QRect(340, 460, 121, 31))
        self.pushButton_Est_Seleccionar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_Est_Seleccionar.setObjectName("pushButton_Est_Seleccionar")
        self.pushButton_Est_Modificar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_Est_Modificar.setGeometry(QtCore.QRect(470, 460, 121, 31))
        self.pushButton_Est_Modificar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_Est_Modificar.setObjectName("pushButton_Est_Modificar")
        self.pushButton_Est_Eliminar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_Est_Eliminar.setGeometry(QtCore.QRect(600, 460, 121, 31))
        self.pushButton_Est_Eliminar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_Est_Eliminar.setObjectName("pushButton_Est_Eliminar")
        self.pushButton_Est_Ingresar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_Est_Ingresar.setGeometry(QtCore.QRect(210, 460, 121, 31))
        self.pushButton_Est_Ingresar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_Est_Ingresar.setObjectName("pushButton_Est_Ingresar")
        self.pushButton_estadioModificar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_estadioModificar.setGeometry(QtCore.QRect(200, 130, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_estadioModificar.setFont(font)
        self.pushButton_estadioModificar.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 203, 203);\n"
"")
        self.pushButton_estadioModificar.setObjectName("pushButton_estadioModificar")
        self.pushButton_estadioEliminar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_estadioEliminar.setGeometry(QtCore.QRect(370, 130, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_estadioEliminar.setFont(font)
        self.pushButton_estadioEliminar.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 203, 203);\n"
"")
        self.pushButton_estadioEliminar.setObjectName("pushButton_estadioEliminar")
        self.pushButton_estadioBuscar = QtWidgets.QPushButton(parent=self.Estadio)
        self.pushButton_estadioBuscar.setGeometry(QtCore.QRect(540, 130, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_estadioBuscar.setFont(font)
        self.pushButton_estadioBuscar.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 127);\n"
"")
        self.pushButton_estadioBuscar.setObjectName("pushButton_estadioBuscar")
        self.tabWidget_Categorias.addTab(self.Estadio, "")
        MainWindow_configuracion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow_configuracion)
        self.statusbar.setObjectName("statusbar")
        MainWindow_configuracion.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_configuracion)
        self.tabWidget_Categorias.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_configuracion)





#------------------------------------------------------------------------------------------------
        #Deshabilito botones Categoria
        self.pushButton_Cat_Ingresar.setEnabled(False)
        self.pushButton_Cat_Seleccionar.setEnabled(False)
        self.pushButton_Cat_Editar.setEnabled(False)
        self.pushButton_Cat_Eliminar.setEnabled(False)
        self.__categorias_controlles.showAllCategorias()

        #Deshabilito botones Tarifas
        self.pushButton_Tar_Ingresar.setEnabled(False)       
        self.pushButton_Tar_Seleccionar.setEnabled(False)
        self.pushButton_Tab_Eliminar.setEnabled(False)
        self.pushButton_Tar_Editar.setEnabled(False) 

        #Deshabilito botones Estadio 
        self.pushButton_estadioModificar.setEnabled(False)
        self.pushButton_estadioEliminar.setEnabled(False)
            
        self.pushButton_verificar.setEnabled(False)
        self.lineEdit_cantSectores.setEnabled(False)
        self.lineEdit_cantFilas.setEnabled(False)
        self.lineEdit_cantButacas.setEnabled(False)
        self.pushButton_confirmar.setEnabled(False)

        self.frame_datosSector.setEnabled(False)

        self.pushButton_Est_Ingresar.setEnabled(False)
        self.pushButton_Est_Seleccionar.setEnabled(False)
        self.pushButton_Est_Eliminar.setEnabled(False)
        self.pushButton_Est_Modificar.setEnabled(False)


        #----------------------------------
        #verifica por enter los edit Categoria
        self.lineEdit_categorias.returnPressed.connect(self.__categorias_controlles.verificarCadenas)
        
        #verifica por enter los edit Tarifa
        self.lineEdit_tipoEntrada.returnPressed.connect(self.__tarifa_controlles.verificarCadenas)
        self.lineEdit_precio.returnPressed.connect(self.__tarifa_controlles.verificarNumeros)        

        #-----------------------------------
        #Botones Categorias
        self.ingresarCat = self.pushButton_Cat_Ingresar.clicked.connect(lambda:self.__categorias_controlles.insertCategoria(self.lineEdit_categorias.text()))
        self.seleccionarCat = self.pushButton_Cat_Seleccionar.clicked.connect(lambda:self.__categorias_controlles.selectCategoria())
        self.modificarCat = self.pushButton_Cat_Editar.clicked.connect(lambda:self.__categorias_controlles.modificarCategoria(self.lineEdit_categorias.text()))
        self.eliminarCat = self.pushButton_Cat_Eliminar.clicked.connect(lambda:self.__categorias_controlles.eliminarCategoria(self.lineEdit_categorias.text()))

         #Botones Tarifas
        self.__tarifa_controlles.showAll_Tarifas() 
        self.ingresarTar = self.pushButton_Tar_Ingresar.clicked.connect(lambda:self.__tarifa_controlles.insertTarifa(self.lineEdit_tipoEntrada.text(),self.lineEdit_precio.text()))
        self.seleccionarTar = self.pushButton_Tar_Seleccionar.clicked.connect(lambda:self.__tarifa_controlles.seleccionarTarifa())
        self.modificarTar = self.pushButton_Tar_Editar.clicked.connect(lambda:self.__tarifa_controlles.modificarTarifa(self.lineEdit_tipoEntrada.text(),self.lineEdit_precio.text()))
        self.eliminarTar = self.pushButton_Tab_Eliminar.clicked.connect(lambda:self.__tarifa_controlles.eliminarTarifa())
        


        #Botones Estadio
        self.lineEdit_nombre.returnPressed.connect(self.__estadios_controlles.validarCadenaNombre)

        self.ingresarEstadio = self.pushButton_estadioIngresar.clicked.connect(lambda:self.__estadios_controlles.insertEstadio(self.lineEdit_nombre.text(),self.lineEdit_direccion.text(),self.lineEdit_telefono.text(),self.lineEdit_correo.text(),self.lineEdit_capTotal.text()))
        self.buscarEstadio = self.pushButton_estadioBuscar.clicked.connect(lambda:self.__estadios_controlles.buscarEstadio(self.lineEdit_nombre.text()))
        self.modificarEstadio = self.pushButton_estadioModificar.clicked.connect(lambda:self.__estadios_controlles.modificarEstadio(self.lineEdit_nombre.text(),self.lineEdit_direccion.text(),self.lineEdit_telefono.text(),self.lineEdit_correo.text(),self.lineEdit_capTotal.text()))
        self.eliminarEstadio = self.pushButton_estadioEliminar.clicked.connect(lambda:self.__estadios_controlles.eliminarEstadio())
        

        #Botones Sectores
        self.lineEdit_cantSectores.returnPressed.connect(self.__sectores_controlles.verificarNumeros)
        self.verificar = self.pushButton_verificar.clicked.connect(lambda:self.__sectores_controlles.verificar(self.lineEdit_capTotal.text(),self.lineEdit_cantSectores.text()))
        self.confirmar = self.pushButton_confirmar.clicked.connect(lambda:self.__sectores_controlles.confirmar())


        self.lineEdit_nombreSector.returnPressed.connect(self.__sectores_controlles.validarNombre)
        self.lineEdit_color.returnPressed.connect(self.__sectores_controlles.validarColor)
        self.lineEdit_precioSector.returnPressed.connect(self.__sectores_controlles.validarPrecio)

        self.ingresarSector = self.pushButton_Est_Ingresar.clicked.connect(lambda:self.__sectores_controlles.insertSectores(self.lineEdit_color.text(),self.lineEdit_nombreSector.text(),self.lineEdit_precioSector.text(),self.lineEdit_nombre.text()))
        self.seleccionSector = self.pushButton_Est_Seleccionar.clicked.connect(lambda:self.__sectores_controlles.seleccionarSector())
        self.modificarSector = self.pushButton_Est_Modificar.clicked.connect(lambda:self.__sectores_controlles.modificarSector(self.lineEdit_nombreSector.text(),self.lineEdit_color.text()))
        self.eliminarSector = self.pushButton_Est_Eliminar.clicked.connect(lambda:self.__sectores_controlles.eliminarSector())
       
       #---------------------------------------------------------------------------------------------------------------
		





















        MainWindow_configuracion.setTabOrder(self.lineEdit_nombre, self.lineEdit_telefono)
        MainWindow_configuracion.setTabOrder(self.lineEdit_telefono, self.lineEdit_capTotal)
        MainWindow_configuracion.setTabOrder(self.lineEdit_capTotal, self.lineEdit_direccion)
        MainWindow_configuracion.setTabOrder(self.lineEdit_direccion, self.lineEdit_correo)
        MainWindow_configuracion.setTabOrder(self.lineEdit_correo, self.pushButton_estadioIngresar)
        MainWindow_configuracion.setTabOrder(self.pushButton_estadioIngresar, self.pushButton_estadioModificar)
        MainWindow_configuracion.setTabOrder(self.pushButton_estadioModificar, self.pushButton_estadioEliminar)
        MainWindow_configuracion.setTabOrder(self.pushButton_estadioEliminar, self.pushButton_estadioBuscar)
        MainWindow_configuracion.setTabOrder(self.pushButton_estadioBuscar, self.lineEdit_cantSectores)
        MainWindow_configuracion.setTabOrder(self.lineEdit_cantSectores, self.pushButton_verificar)
        MainWindow_configuracion.setTabOrder(self.pushButton_verificar, self.lineEdit_cantFilas)
        MainWindow_configuracion.setTabOrder(self.lineEdit_cantFilas, self.lineEdit_cantButacas)
        MainWindow_configuracion.setTabOrder(self.lineEdit_cantButacas, self.pushButton_confirmar)
        MainWindow_configuracion.setTabOrder(self.pushButton_confirmar, self.lineEdit_nombreSector)
        MainWindow_configuracion.setTabOrder(self.lineEdit_nombreSector, self.lineEdit_precioSector)
        MainWindow_configuracion.setTabOrder(self.lineEdit_precioSector, self.lineEdit_color)
        MainWindow_configuracion.setTabOrder(self.lineEdit_color, self.pushButton_Est_Ingresar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Est_Ingresar, self.pushButton_Est_Seleccionar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Est_Seleccionar, self.pushButton_Est_Modificar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Est_Modificar, self.pushButton_Est_Eliminar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Est_Eliminar, self.tableWidget_estadio)
        MainWindow_configuracion.setTabOrder(self.tableWidget_estadio, self.pushButton_Cat_Ingresar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Cat_Ingresar, self.pushButton_Cat_Seleccionar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Cat_Seleccionar, self.tableWidget_categorias)
        MainWindow_configuracion.setTabOrder(self.tableWidget_categorias, self.lineEdit_categorias)
        MainWindow_configuracion.setTabOrder(self.lineEdit_categorias, self.lineEdit_precio)
        MainWindow_configuracion.setTabOrder(self.lineEdit_precio, self.pushButton_Tar_Editar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Tar_Editar, self.pushButton_Tab_Eliminar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Tab_Eliminar, self.tabWidget_Categorias)
        MainWindow_configuracion.setTabOrder(self.tabWidget_Categorias, self.pushButton_Tar_Ingresar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Tar_Ingresar, self.pushButton_Tar_Seleccionar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Tar_Seleccionar, self.pushButton_Cat_Editar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Cat_Editar, self.pushButton_Cat_Eliminar)
        MainWindow_configuracion.setTabOrder(self.pushButton_Cat_Eliminar, self.tableWidget_tarifas)
        MainWindow_configuracion.setTabOrder(self.tableWidget_tarifas, self.lineEdit_tipoEntrada)

    def retranslateUi(self, MainWindow_configuracion):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_configuracion.setWindowTitle(_translate("MainWindow_configuracion", "CONFIGURACION"))
        self.tableWidget_categorias.setSortingEnabled(True)
        item = self.tableWidget_categorias.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_configuracion", "Categoria"))
        self.label_2.setText(_translate("MainWindow_configuracion", "CATEGORIAS:"))
        self.pushButton_Cat_Ingresar.setText(_translate("MainWindow_configuracion", "INGRESAR"))
        self.pushButton_Cat_Seleccionar.setText(_translate("MainWindow_configuracion", "SELECCIONAR"))
        self.pushButton_Cat_Editar.setText(_translate("MainWindow_configuracion", "EDITAR"))
        self.pushButton_Cat_Eliminar.setText(_translate("MainWindow_configuracion", "ELIMINAR"))
        self.label_26.setText(_translate("MainWindow_configuracion", "Ingrese ENTER al finalizar"))
        self.tabWidget_Categorias.setTabText(self.tabWidget_Categorias.indexOf(self.Categorias), _translate("MainWindow_configuracion", "Categorias"))
        self.label_3.setText(_translate("MainWindow_configuracion", "PRECIO:   $"))
        self.label.setText(_translate("MainWindow_configuracion", "TIPO ENTRADA:"))
        self.tableWidget_tarifas.setSortingEnabled(True)
        item = self.tableWidget_tarifas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_configuracion", "Tipo Entrada"))
        item = self.tableWidget_tarifas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_configuracion", "Precio"))
        self.pushButton_Tar_Ingresar.setText(_translate("MainWindow_configuracion", "INGRESAR"))
        self.pushButton_Tab_Eliminar.setText(_translate("MainWindow_configuracion", "ELIMINAR"))
        self.pushButton_Tar_Editar.setText(_translate("MainWindow_configuracion", "EDITAR"))
        self.pushButton_Tar_Seleccionar.setText(_translate("MainWindow_configuracion", "SELECCIONAR"))
        self.label_24.setText(_translate("MainWindow_configuracion", "Ingrese ENTER al finalizar"))
        self.label_25.setText(_translate("MainWindow_configuracion", "Formato 0000.00 . ENTER al final"))
        self.tabWidget_Categorias.setTabText(self.tabWidget_Categorias.indexOf(self.Tarifas), _translate("MainWindow_configuracion", "Tarifas"))
        self.label_12.setText(_translate("MainWindow_configuracion", "* Verificar cantidad de Filas y Butacas, por sector."))
        self.tableWidget_estadio.setSortingEnabled(True)
        item = self.tableWidget_estadio.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_configuracion", "SECTOR"))
        item = self.tableWidget_estadio.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_configuracion", "COLOR"))
        item = self.tableWidget_estadio.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_configuracion", "FILA INICIO"))
        item = self.tableWidget_estadio.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_configuracion", "FILA FINAL"))
        item = self.tableWidget_estadio.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_configuracion", "BUTACAS"))
        self.label_7.setText(_translate("MainWindow_configuracion", "CANT. FILAS:  *"))
        self.label_8.setText(_translate("MainWindow_configuracion", "CANT. BUTACAS: *"))
        self.label_4.setText(_translate("MainWindow_configuracion", "NOMBRE:"))
        self.label_5.setText(_translate("MainWindow_configuracion", "DIRECCION:"))
        self.pushButton_verificar.setText(_translate("MainWindow_configuracion", "VERIFICAR "))
        self.pushButton_confirmar.setText(_translate("MainWindow_configuracion", "CONFIRMAR"))
        self.pushButton_estadioIngresar.setText(_translate("MainWindow_configuracion", "INGRESAR ESTADIO"))
        self.label_6.setText(_translate("MainWindow_configuracion", "TELEFONO:"))
        self.label_9.setText(_translate("MainWindow_configuracion", "CAP. TOTAL:"))
        self.label_10.setText(_translate("MainWindow_configuracion", "CANT. SECTORES:"))
        self.label_11.setText(_translate("MainWindow_configuracion", "COLOR:"))
        self.label_13.setText(_translate("MainWindow_configuracion", "PRECIO SECTOR:"))
        self.label_14.setText(_translate("MainWindow_configuracion", "NOMBRE SECTOR:"))
        self.label_15.setText(_translate("MainWindow_configuracion", "CORREO:"))
        self.pushButton_Est_Seleccionar.setText(_translate("MainWindow_configuracion", "Seleccionar Sector"))
        self.pushButton_Est_Modificar.setText(_translate("MainWindow_configuracion", "Modificar Sector"))
        self.pushButton_Est_Eliminar.setText(_translate("MainWindow_configuracion", "Eliminar Sector"))
        self.pushButton_Est_Ingresar.setText(_translate("MainWindow_configuracion", "Ingresar Sector"))
        self.pushButton_estadioModificar.setText(_translate("MainWindow_configuracion", "MODIFICAR ESTADIO"))
        self.pushButton_estadioEliminar.setText(_translate("MainWindow_configuracion", "ELIMINAR ESTADIO"))
        self.pushButton_estadioBuscar.setText(_translate("MainWindow_configuracion", "BUSCAR ESTADIO"))
        self.tabWidget_Categorias.setTabText(self.tabWidget_Categorias.indexOf(self.Estadio), _translate("MainWindow_configuracion", "Estadio"))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        menuConfiguracion= QtWidgets.QMainWindow()
        ui = Ui_MainWindow_configuracion()
        ui.setupUi(menuConfiguracion)      
        menuConfiguracion.show()
        sys.exit(app.exec())