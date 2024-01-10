class Programacion():

    def __init__(self,bd_conexion):
        self.bd_conexion = bd_conexion
        
        with self.bd_conexion.cursor() as cursor:
            print("cursor",cursor)
            sql = """CREATE TABLE IF NOT EXISTS Programacion
                    (
                   id int auto_increment  NOT NULL,
                    evento varchar(50) NOT NULL,
                    fecha  date not  null,
                    categoria varchar(50) not null,
                    nombre varchar (50) not null,
                    horaInicio time not null,
                    eliminado varchar(10) not null, 
                    primary key (id)                   
                    )"""
            cursor.execute(sql)
            self.bd_conexion.commit() 

    def horarioDisponible(self,evento,dia,categoria):
        with self.bd_conexion.cursor() as cursor:   
            sql = """SELECT horaInicio  FROM  programacion where evento =%s and fecha =%s and categoria =%s  """
            cursor.execute(sql,(evento,dia,categoria)) 
            resultado = cursor.fetchall()  
            print("hora inicio de un evento:",resultado)
            return resultado   

    def bandahabilitada(self,evento,fecha,categoria,nombre):
        with self.bd_conexion.cursor() as cursor:   
            sql = """SELECT horaInicio,fecha,evento,nombre  FROM  programacion where evento =%s and fecha =%s and categoria =%s and nombre =%s """
            cursor.execute(sql,(evento,fecha,categoria,nombre)) 
            resultado = cursor.fetchall()  
            print("Banda:",resultado)
            return resultado  
        
    
        
    def cargarProgramacion(self,evento,fecha,categoria,nombre,horaResultado):
        eliminado = "No"
        with self.bd_conexion.cursor() as cursor:         
            sql = """INSERT INTO programacion(evento,fecha,categoria,nombre,horaInicio,eliminado) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql,(evento,fecha,categoria,nombre,horaResultado,eliminado))
            self.bd_conexion.commit()
    
    def getProgramacion(self):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT id,evento,fecha,categoria,nombre,horaInicio FROM programacion where eliminado = 'No' """           
            cursor.execute(sql)
            resultado = cursor.fetchall()                                
            return resultado 
        
    def get_programacionbyId(self,id_num) :
        print(id_num)
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT evento,fecha,categoria,nombre FROM programacion where id= %s and eliminado = 'No' """           
            cursor.execute(sql,(id_num,))
            resultado = cursor.fetchall()                                
            return resultado 
        
    def modificar(self,evento,fecha,categoria,nombre,id_programacion):
        with self.bd_conexion.cursor() as cursor:            
            sql = """UPDATE programacion SET evento = %s, fecha = %s, categoria = %s, nombre = %s  WHERE id = %s """           
            cursor.execute(sql,(evento,fecha,categoria,nombre,id_programacion))
            self.bd_conexion.commit() 
            
    def eliminar(self,id_programacion,eliminado):
         with self.bd_conexion.cursor() as cursor:            
            sql = """UPDATE programacion SET eliminado = %s  WHERE id = %s """           
            cursor.execute(sql,(eliminado,id_programacion))
            self.bd_conexion.commit() 