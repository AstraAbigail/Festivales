class Categorias():

    def __init__(self,bd_conexion):
        self.bd_conexion = bd_conexion
        
        with self.bd_conexion.cursor() as cursor:
            print("cursor",cursor)
            sql = """CREATE TABLE IF NOT EXISTS Categorias
                    (
                    id  int auto_increment NOT NULL,
                    descripcion VARCHAR(30) NOT NULL,
                    primary key (id) 
                    )"""
            cursor.execute(sql)
            self.bd_conexion.commit() 

    def getCategoriaSpecific(self,descripcion):
         with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT * FROM Categorias WHERE descripcion = %s """
            cursor.execute(sql,(descripcion,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            if resultado:
                return resultado    
            
    def insertCategoria(self,descripcion):
        with self.bd_conexion.cursor() as cursor:         
            sql = """INSERT INTO Categorias(descripcion) VALUES (%s)"""
            cursor.execute(sql,(descripcion,))
            self.bd_conexion.commit()
    
    #RETORNA EL ID DE LA CATEGORIA
    def getIdCategoriaSpecific(self,descripcion):
         with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT id FROM Categorias WHERE descripcion = %s """
            cursor.execute(sql,(descripcion,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            if resultado:
                return resultado 


    def modificarCategoria(self,descripcion,id_):
        #print(descripcion,id_)
        with self.bd_conexion.cursor() as cursor:         
            sql =""" UPDATE Categorias SET descripcion = %s WHERE id = %s """
            cursor.execute(sql,(descripcion,id_))
            self.bd_conexion.commit()

    def eliminarCategoria(self,descripcion,id):
        with self.bd_conexion.cursor() as cursor:         
            sql =""" DELETE FROM Categorias WHERE id = %s and descripcion = %s """
            cursor.execute(sql,(id,descripcion))
            self.bd_conexion.commit()

    def getCategorias(self):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT descripcion FROM Categorias """           
            cursor.execute(sql)
            resultado = cursor.fetchall()
            #print("resultado",resultado)                     
            return resultado
        
    def cargarComboCategorias(self):
        with self.bd_conexion.cursor() as cursor:                       
            sql = """SELECT descripcion FROM  categorias """
            cursor.execute(sql) 
            resultado = cursor.fetchall()  
            print("combo box categorias",resultado)
            return resultado 
        
    def getNameCategoriaByID(self,id_):
        with self.bd_conexion.cursor() as cursor:                       
            sql = """SELECT descripcion FROM  categorias where id=%s """
            cursor.execute(sql,(id_,)) 
            resultado = cursor.fetchone()  
          
            return resultado 

            