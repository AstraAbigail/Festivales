



class Estadios():

    def __init__(self,bd_conexion):
        self.bd_conexion = bd_conexion
        
        
        with self.bd_conexion.cursor() as cursor:
            print("cursor",cursor)
            sql = """CREATE TABLE IF NOT EXISTS Estadios
                    (
                    id int auto_increment  NOT NULL,
                    nombre VARCHAR(50) NOT NULL,
                    direccion VARCHAR(50) not null,
                    correo varchar(50) not null,
                    telefono int not null,
                    capTotal int not null,
                    primary key (id) 
                    )"""
            cursor.execute(sql)
            self.bd_conexion.commit() 
    
    def insert(self,nombre,direccion,telefono,correo,capTotal):
        with self.bd_conexion.cursor() as cursor:         
            sql = """INSERT INTO Estadios(nombre,direccion,correo,telefono,capTotal) VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(sql,(nombre,direccion,correo,telefono,capTotal))
            self.bd_conexion.commit()
    
    def searchByName(self,nombre):
        with self.bd_conexion.cursor() as cursor:         
                sql = """SELECT * FROM Estadios WHERE nombre = %s """
                cursor.execute(sql,(nombre,))                  
                resultado = cursor.fetchone()
                #print("resultado",resultado)                     
                return resultado 
    
    def searchIdByName(self,nombre):
        with self.bd_conexion.cursor() as cursor:         
                sql = """SELECT id FROM Estadios WHERE nombre = %s """
                cursor.execute(sql,(nombre,))                  
                resultado = cursor.fetchone()
                #print("resultado",resultado)                     
                return resultado 
        
    def modificar(self,direccion,telefono,correo,capTotal,id_):
        with self.bd_conexion.cursor() as cursor:         
                    sql = """UPDATE Estadios SET  direccion = %s, correo = %s, telefono = %s, capTotal = %s  WHERE id = %s"""
                    cursor.execute(sql,(direccion,correo,telefono,capTotal,id_))
                    self.bd_conexion.commit()  
    
    def eliminar(self,id):
           print(id)
           with self.bd_conexion.cursor() as cursor:         
                    sql = """ DELETE FROM Estadios WHERE id= %s"""
                    cursor.execute(sql,(id,))
                    self.bd_conexion.commit() 
                    return True
    
    def cargarComboEstadios(self):
        with self.bd_conexion.cursor() as cursor:                       
            sql = """SELECT nombre FROM  estadios """
            cursor.execute(sql) 
            resultado = cursor.fetchall()  
            print("combo box estadios:",resultado)
            return resultado
        
    def getNameEventoById(self,id_evento):
        with self.bd_conexion.cursor() as cursor:                       
                sql = """SELECT nombre FROM  estadios WHERE id = %s """
                cursor.execute(sql,(id_evento,)) 
                resultado = cursor.fetchall()
                #print("estadio:",resultado)               
                return resultado
   
           
    