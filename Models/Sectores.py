

class Sectores():

    def __init__(self,bd_conexion):
        self.bd_conexion = bd_conexion
       
        
        with self.bd_conexion.cursor() as cursor:
            print("cursor",cursor)
            sql = """CREATE TABLE IF NOT EXISTS Sectores
                    (
                    id int auto_increment  NOT NULL,
                    color VARCHAR(30) NOT NULL,
                    nombre VARCHAR(50),
                    fila_inicio int not null,
                    fila_fin int not null,
                    precio decimal (7,2) not null,
                    butacas int not null,
                    estadio int not null,
                    eliminado varchar(10) not null,
                    primary key (id) ,
                    FOREIGN KEY (estadio) REFERENCES estadios(id) 
                    )"""
            cursor.execute(sql)
            self.bd_conexion.commit() 


    def filas(self,id_estadio):       
        with self.bd_conexion.cursor(buffered=True) as cursor:         
                sql = """SELECT fila_inicio,fila_fin  FROM Sectores WHERE estadio = %s and eliminado = 'No' """
                cursor.execute(sql,(id_estadio,))                  
                resultado = cursor.fetchall()
                print("resultado query sectores:",resultado)                     
                return resultado 
    
    def searchIdEstadiobyName(self,nombreEstadio):
        with self.bd_conexion.cursor() as cursor:         
                sql = """SELECT id  FROM Estadios WHERE nombre = %s """
                cursor.execute(sql,(nombreEstadio,))                  
                resultado = cursor.fetchone()
                #print("resultado query sectores id estadio :",resultado)                     
                return resultado 
    
    def insertSector(self,color,nombre,fila_inicio,fila_fin,precio,butacas,id_estadio,eliminado):
        with self.bd_conexion.cursor() as cursor:         
            sql = """INSERT INTO Sectores(color,nombre,fila_inicio,fila_fin,precio,butacas,estadio,eliminado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql,(color,nombre,fila_inicio,fila_fin,precio,butacas,id_estadio,eliminado))
            self.bd_conexion.commit()

    def getSectoresByIdEstadio(self, id_estadio):
         #seleccinar de un mismo estadio los sectores 
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT DISTINCT sectores.nombre ,sectores.color,sectores.fila_inicio,sectores.fila_fin ,sectores.butacas 
                    FROM sectores
                    INNER JOIN estadios ON sectores.estadio = %s
                    where eliminado = 'No' """
            cursor.execute(sql,(id_estadio,))                  
            resultado = cursor.fetchall()
            #print("resultado query sectores todos los sectores:",resultado)                     
            return resultado 
    
    def contarSectorByIdEstacion(self,id_estadio):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT nombre from sectores where estadio = %s and eliminado = 'No' """           
            cursor.execute(sql,(id_estadio,))                  
            resultado = cursor.fetchall()
            print("count sector por estadio:",resultado)                     
            return resultado 
        
    def butacasByEstadio(self,id_estadio):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT butacas from sectores where estadio = %s;"""           
            cursor.execute(sql,(id_estadio,))                  
            resultado = cursor.fetchone()
            print("butacas:",resultado)                     
            return resultado 
       
        
    def SearchNameSectorByName(self,id_estadio):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT DISTINCT nombre from sectores where estadio = %s and eliminado = 'No' """           
            cursor.execute(sql,(id_estadio,))                  
            resultado = cursor.fetchall()
            print("nombre:",resultado)                     
            return resultado 
    def SearchColorSectorByName(self,id_estadio):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT color from sectores where estadio = %s and eliminado = 'No' """           
            cursor.execute(sql,(id_estadio,))                  
            resultado = cursor.fetchall()
            print("color:",resultado)                     
            return resultado
    
    def IDsectorByName(self,nombre,intestadio):
         with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT id from sectores where nombre = %s and estadio = %s and eliminado = 'No' """           
            cursor.execute(sql,(nombre,intestadio))                  
            resultado = cursor.fetchone()
            print("id_sector _query :",resultado)                     
            return resultado
         
    def getSpecificSectorById(self,id):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECt nombre,color,precio from sectores where id = %s"""           
            cursor.execute(sql,(id,))                  
            resultado = cursor.fetchall()
            #print("sector especifico :",resultado)                     
            return resultado
         
    def searchIdEstadiobyName(self,nombre_estadio):    
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT id from estadios where nombre = %s"""           
            cursor.execute(sql,(nombre_estadio,))                  
            resultado = cursor.fetchone()
            #print("id :",resultado)                     
            return resultado
    def searchNameinSectorbyIdEstacion(self,id_):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECt nombre from sectores where estadio = %s"""           
            cursor.execute(sql,(id_,))                  
            resultado = cursor.fetchall()
            #print("nombres :",resultado)                     
            return resultado
    def searchColorsSectorsbyIdEstacion(self,id_):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECt color from sectores where estadio = %s"""           
            cursor.execute(sql,(id_,))                  
            resultado = cursor.fetchall()
            #print("colores:",resultado)                     
            return resultado
    def modificarSector(self,nombreSector,colorSector,id_):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql =""" UPDATE sectores SET color = %s, nombre = %s  WHERE id = %s """
            cursor.execute(sql,(colorSector,nombreSector,id_))
            self.bd_conexion.commit()
    
    
    def cargarComboBox(self,id_estadio):   
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECt nombre,precio from sectores where estadio = %s"""           
            cursor.execute(sql,(id_estadio,))                  
            resultado = cursor.fetchall()
            #print("colores:",resultado)                     
            return resultado
        
    def cargarComboBoxFila(self,cadena):  
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECt fila_inicio,fila_fin,precio from sectores where nombre = %s"""           
            cursor.execute(sql,(cadena,))                  
            resultado = cursor.fetchall()
            #print("colores:",resultado)                     
            return resultado
        
    def getButacas(self,sector):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT butacas from sectores where nombre = %s"""           
            cursor.execute(sql,(sector,))                  
            resultado = cursor.fetchone()
            #print("colores:",resultado)                     
            return resultado
    
    def colorByID(self,cadena):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT color from sectores where id = %s"""           
            cursor.execute(sql,(cadena,))                  
            resultado = cursor.fetchone()
            #print("colores:",resultado)                     
            return resultado
        
    def precioSector(self,cadena):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT precio from sectores where nombre = %s"""           
            cursor.execute(sql,(cadena,))                  
            resultado = cursor.fetchone()
            #print("colores:",resultado)                     
            return resultado
        
    def getNameById(self,id):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT nombre from sectores where id = %s"""           
            cursor.execute(sql,(id,))                  
            resultado = cursor.fetchone()
            #print("colores:",resultado)                     
            return resultado
        
    def Color_NombreBy_Estadio(self,id_estadio):
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql = """SELECT nombre,color from sectores where estadio = %s"""           
            cursor.execute(sql,(id_estadio,))                  
            resultado = cursor.fetchone()
            #print("colores:",resultado)                     
            return resultado
    
    def eliminarSector(self,eliminado,cod_sector):
        with self.bd_conexion.cursor() as cursor:         
            sql =""" UPDATE sectores SET eliminado = %s  WHERE id = %s """
            cursor.execute(sql,(eliminado,cod_sector))
            self.bd_conexion.commit()

    def id_eventoYnombre(self,id_evento,sector_chequeo):
            with self.bd_conexion.cursor(buffered=True) as cursor:         
                        sql = """SELECT id from sectores where estadio = %s and nombre =%s and eliminado = 'No'  """           
                        cursor.execute(sql,(id_evento,sector_chequeo))                  
                        resultado = cursor.fetchone()
                        print("ID NUEVO:",resultado)                     
                        return resultado
    def cargarComboBoxNoEliminados(self,idEstadio):
          with self.bd_conexion.cursor() as cursor:         
                sql = """SELECT nombre from sectores where estadio = %s and eliminado = 'No'  """           
                cursor.execute(sql,(idEstadio,))                  
                resultado = cursor.fetchall()
                print("combo box  NUEVO:",resultado)                     
                return resultado