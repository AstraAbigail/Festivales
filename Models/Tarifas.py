class Tarifas():

    def __init__(self,bd_conexion):
        self.bd_conexion = bd_conexion
        
        with self.bd_conexion.cursor() as cursor:
            print("cursor",cursor)
            sql = """CREATE TABLE IF NOT EXISTS Tarifas
                    (
                    id INT  auto_increment NOT NULL,
                    descripcion VARCHAR(30) NOT NULL,
                    precio DECIMAL(5,2) NOT NULL,
                    primary key (id) )"""
            cursor.execute(sql)
            self.bd_conexion.commit()

    
    def getTarifa(self,descripcion,precio):
        with self.bd_conexion.cursor() as cursor:                      
            sql = """ SELECT * FROM Tarifas WHERE descripcion = %s """
            cursor.execute(sql,(descripcion,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            print("resultado de la query: ",resultado)
            if resultado:
                return resultado 
    
    def searchTarifaByName(self,descripcion):
        with self.bd_conexion.cursor(buffered=True) as cursor:                      
                sql = """ SELECT * FROM Tarifas WHERE descripcion = %s """
                cursor.execute(sql,(descripcion,)) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchone()
                #print("resultado de la query: ",resultado)
                if resultado:
                    return resultado 


    def insertTarifa(self,descripcion,precio):
        with self.bd_conexion.cursor() as cursor:         
            sql = """INSERT INTO Tarifas(descripcion,precio) VALUES (%s,%s)"""
            cursor.execute(sql,(descripcion,precio))
            self.bd_conexion.commit()

    def getTarifas(self):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT descripcion,precio FROM Tarifas """           
            cursor.execute(sql)
            resultado = cursor.fetchall()
            #print("resultado",resultado)                     
            return resultado 
        
    def getTarifaSpecific(self,id):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT * FROM Tarifas WHERE id = %s """
            cursor.execute(sql,(id,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            print(resultado)
            if resultado:
                return resultado       
    
    def getIdTarifaSpecific(self,descripcion):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT id FROM Tarifas WHERE descripcion = %s """
            cursor.execute(sql,(descripcion,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            if resultado:
                return resultado 
            
    def getTarifaSpecificbyName(self,id):
        with self.bd_conexion.cursor(buffered=True) as cursor:            
                    sql = """ SELECT descripcion, precio FROM Tarifas WHERE id = %s """
                    cursor.execute(sql,(id,)) #mysql  necesita una tupla, minimamente o list o diccionario
                    resultado = cursor.fetchone()
                    #print("resultado Query by Name",resultado)
                    if resultado:
                        return resultado 

    def modificarTarifa(self,descripcion,precio,id_):        
        with self.bd_conexion.cursor(buffered=True) as cursor:         
            sql =""" UPDATE Tarifas SET descripcion = %s, precio = %s  WHERE id = %s """
            cursor.execute(sql,(descripcion,precio,id_))
            self.bd_conexion.commit()

    def eliminarTarifa(self,id_):
        with self.bd_conexion.cursor() as cursor:       
            sql =""" DELETE FROM Tarifas WHERE id= %s """
            cursor.execute(sql,(id_,))
            self.bd_conexion.commit()
    
    def cargarComboBox(self):
         with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT descripcion FROM Tarifas"""
            cursor.execute(sql) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchall()
            if resultado:
                return resultado 
    def precioByTipo(self,cadena):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT precio FROM Tarifas where descripcion = %s """
            cursor.execute(sql,(cadena,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            if resultado:
                return resultado
    def getNameById(self,id_tipoEntrada):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT descripcion FROM Tarifas where id = %s """
            cursor.execute(sql,(id_tipoEntrada,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            if resultado:
                return resultado