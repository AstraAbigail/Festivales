class Inscrpciones():

    def __init__(self,bd_conexion):
        self.bd_conexion = bd_conexion
        
        with self.bd_conexion.cursor() as cursor:
            print("cursor",cursor)
            sql = """create table IF NOT EXISTS Inscripciones(
                    id int auto_increment  NOT NULL,
                    categoria varchar(50) NOT NULL,
                    nombre varchar(50) not null,
                    detalle  varchar(100) not null,
                    correo  varchar(50)  not null,
                    eliminado varchar(10) not null,
                    primary key (id) 
                    )"""
            cursor.execute(sql)
            self.bd_conexion.commit() 
        
    def showId_InscripcionesByNombreCategoria(self,nombre,categoria):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT id FROM inscripciones where nombre = %s and categoria =%s """           
            cursor.execute(sql,(nombre,categoria))
            resultado = cursor.fetchone()  
            print(resultado)                              
            return resultado
        
    def cargar(self,categoria,nombre,detalle,correo,eliminado):
        with self.bd_conexion.cursor() as cursor:         
                    sql = """INSERT INTO inscripciones (categoria,nombre,detalle,correo,eliminado) VALUES (%s,%s,%s,%s,%s)"""
                    cursor.execute(sql,(categoria,nombre,detalle,correo,eliminado))
                    self.bd_conexion.commit()

    def getInscriptos(self): 
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT nombre,correo,detalle,categoria FROM inscripciones  where eliminado = 'No' """           
            cursor.execute(sql)
            resultado = cursor.fetchall()                                
            return resultado 
        
    def getIdInscripcionSpecific(self,descripcion):
        with self.bd_conexion.cursor(buffered=True) as cursor:            
            sql = """ SELECT id FROM inscripciones WHERE nombre = %s """
            cursor.execute(sql,(descripcion,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            if resultado:
                #print(resultado[0])
                return resultado[0]   
            
    def getInscripcionSpecificById(self,id): 
         with self.bd_conexion.cursor(buffered=True) as cursor:            
                sql = """ SELECT nombre,correo,detalle,categoria FROM inscripciones  WHERE id = %s """
                cursor.execute(sql,(id,)) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchall()
                #print("resultado Query by Name",resultado)
                if resultado:
                    return resultado 
                
    def modificar(self,categoria,nombre,detalle,correo,id): 
        with self.bd_conexion.cursor() as cursor:         
                sql = """UPDATE inscripciones SET categoria = %s, nombre = %s, detalle = %s, correo = %s  WHERE id = %s"""
                #cursor.execute(sql,(nombre,lugar,categoria,fechaInicio,hora,fechaFinal,id_evento))
                cursor.execute(sql,(categoria,nombre,detalle,correo,id))
                self.bd_conexion.commit() 

    def eliminar(self,eliminado,id_inscripcion):
        with self.bd_conexion.cursor() as cursor:         
                sql = """UPDATE inscripciones SET eliminado = %s  WHERE id = %s"""               
                cursor.execute(sql,(eliminado,id_inscripcion))
                self.bd_conexion.commit()  
    
    def cargarComboNombres(self,categoria):
        with self.bd_conexion.cursor() as cursor:                       
            sql = """SELECT nombre FROM  inscripciones where categoria = %s """
            cursor.execute(sql,(categoria,)) 
            resultado = cursor.fetchall()  
            print("combo box categorias",resultado)
            return resultado 
        
    def getNameById(self,id_nombre):
        with self.bd_conexion.cursor() as cursor:                       
            sql = """SELECT nombre FROM  inscripciones where id = %s """
            cursor.execute(sql,(id_nombre,)) 
            resultado = cursor.fetchone()              
            return resultado 
    
    def getIdByName(self,nombre):
        with self.bd_conexion.cursor() as cursor:                       
            sql = """SELECT id FROM  inscripciones where nombre = %s """
            cursor.execute(sql,(nombre,)) 
            resultado = cursor.fetchone()              
            return resultado 
        