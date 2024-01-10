class Eventos():

    def __init__(self,bd_conexion):
        self.bd_conexion = bd_conexion
        
        with self.bd_conexion.cursor() as cursor:
            print("cursor",cursor)
            sql = """CREATE TABLE IF NOT EXISTS Eventos
                    (
                    id int auto_increment  NOT NULL,
                    nombre  varchar(50) NOT NULL,
                    lugar varchar(50) not null,
                    categoria varchar(50) not null,
                    fecha date not null,
                    hora time not null,
                    fechaFinal date not null, 
                    eliminado varchar(10) not null,
                    primary key (id)             
                    )"""
            cursor.execute(sql)
            self.bd_conexion.commit()

    def cargar(self,nombre,lugar,categoria,fechaini,fechafin,horainicio,eliminado):
        fecha_conversionIni = fechaini.text()
        fecha_conversionFin = fechafin.text()
        with self.bd_conexion.cursor() as cursor:         
            sql = """INSERT INTO eventos(nombre,lugar,categoria,fecha,hora,fechaFinal,eliminado) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql,(nombre,lugar,categoria,fecha_conversionIni,horainicio,fecha_conversionFin,eliminado))
            self.bd_conexion.commit()
    
    def getEvents(self):  
         with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT nombre,lugar,categoria,fecha,hora,fechaFinal FROM Eventos where eliminado = 'No' """           
            cursor.execute(sql)
            resultado = cursor.fetchall()
                                
            return resultado 
         
    def getIdEventoSpecific(self,descripcion):  
        with self.bd_conexion.cursor(buffered=True) as cursor:            
            sql = """ SELECT id FROM eventos WHERE nombre = %s """
            cursor.execute(sql,(descripcion,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            if resultado:
                print(resultado[0])
                return resultado[0] 
    
    def getEventoSpecificById(self,id_evento): 
        with self.bd_conexion.cursor(buffered=True) as cursor:            
                sql = """ SELECT nombre,lugar,categoria,fecha,fechaFinal FROM eventos  WHERE id = %s """
                cursor.execute(sql,(id_evento,)) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchall()
                #print("resultado Query by Name",resultado)
                if resultado:
                    return resultado 
                    
    def showEventsByName(self,nombre):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT nombre,lugar FROM Eventos where nombre = %s """           
            cursor.execute(sql,(nombre,))
            resultado = cursor.fetchall()                                
            return resultado 
        
    def getIdEventByLugar(self,lugar,nombre):
        with self.bd_conexion.cursor(buffered=True) as cursor:            
                sql = """ SELECT id FROM eventos  WHERE lugar = %s and nombre = %s """
                cursor.execute(sql,(lugar,nombre)) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchall()               
                if resultado:
                    print(resultado)
                    return resultado 
                
    def getIdEventByName(self,nombre):
        with self.bd_conexion.cursor(buffered=True) as cursor:            
                sql = """ SELECT id FROM eventos  WHERE  nombre = %s """
                cursor.execute(sql,(nombre,)) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchall()               
                if resultado:
                    print(resultado)
                    return resultado 
                
    def modificar(self,nombre,lugar,categoria,fechaIni,hora,fechaFin,id_evento):
            #fechaInicio = fechaIni.text()
            #fechaFinal  = fechaFin.text()            
            with self.bd_conexion.cursor() as cursor:         
                sql = """UPDATE eventos SET nombre = %s, lugar = %s, categoria = %s, fecha = %s, hora = %s, fechaFinal = %s  WHERE id = %s"""
                #cursor.execute(sql,(nombre,lugar,categoria,fechaInicio,hora,fechaFinal,id_evento))
                cursor.execute(sql,(nombre,lugar,categoria,fechaIni,hora,fechaFin,id_evento))
                self.bd_conexion.commit()  

    def eliminar(self,eliminado,id_evento):
         with self.bd_conexion.cursor() as cursor:         
                sql = """UPDATE eventos SET eliminado = %s  WHERE id = %s"""               
                cursor.execute(sql,(eliminado,id_evento))
                self.bd_conexion.commit() 

    def cargarComboEventosNombres(self):
       with self.bd_conexion.cursor() as cursor:                       
            sql = """SELECT nombre FROM  eventos """
            cursor.execute(sql) 
            resultado = cursor.fetchall()  
            print("combo box:",resultado)
            return resultado 
       
    def getDateInicio(self,id):
        with self.bd_conexion.cursor() as cursor:   
            sql = """SELECT fecha  FROM  eventos where id =%s """
            cursor.execute(sql,(id,)) 
            resultado = cursor.fetchone()  
            print("date Inicio:",resultado)
            return resultado[0]
         
    def getDateFinal(self,id):
        with self.bd_conexion.cursor() as cursor:   
            sql = """SELECT fechaFinal  FROM  eventos where id =%s """
            cursor.execute(sql,(id,)) 
            resultado = cursor.fetchone()  
            print("date Final:",resultado)
            return resultado[0]      
    def getHoraInicial(self,id):
        with self.bd_conexion.cursor() as cursor:   
            sql = """SELECT hora  FROM  eventos where id =%s  """
            cursor.execute(sql,(id,)) 
            resultado = cursor.fetchone()  
            print("hora:",resultado)
            return resultado[0]
     
    def getHoraInicialByFecha(self,id,fecha):
        with self.bd_conexion.cursor() as cursor:   
            sql = """SELECT hora  FROM  eventos where id =%s and fecha =%s """
            cursor.execute(sql,(id,fecha)) 
            resultado = cursor.fetchone()  
            print("hora:",resultado)
            return resultado[0]
        
    def cargarComboEstadiosNombres(self,cadena):
        with self.bd_conexion.cursor() as cursor:                       
            sql = """SELECT lugar FROM  eventos WHERE nombre = %s """
            cursor.execute(sql,(cadena,)) 
            resultado = cursor.fetchall()  
            print("combo box, Tickets estadios:",resultado)
            return resultado
        
    def getNameFestivalById(self,id_festival):
         with self.bd_conexion.cursor() as cursor:                       
                sql = """SELECT nombre FROM  eventos WHERE id = %s """
                cursor.execute(sql,(id_festival,)) 
                resultado = cursor.fetchone()
                #print("festival",resultado)               
                return resultado
    

    
      