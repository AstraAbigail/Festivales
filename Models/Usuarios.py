class Usuarios():

    def __init__(self,bd_conexion):
        self.bd_conexion = bd_conexion
        
        with self.bd_conexion.cursor() as cursor:
            print("cursor",cursor)
            sql = """CREATE TABLE IF NOT EXISTS Usuarios
                    (
                    id int  auto_increment  NOT NULL,
                    nombre VARCHAR (30) NOT NULL,
                    correo  VARCHAR (50) NOT NULL,
                    usuario VARCHAR (30) NOT NULL,
                    contraseña VARCHAR (30) NOT NULL,
                    crearEvento VARCHAR (1) NOT NULL,
                    programacion VARCHAR (1) NOT NULL,
                    inscripciones VARCHAR (1) NOT NULL,
                    configuracion VARCHAR (1) NOT NULL,
                    tickets VARCHAR (1) NOT NULL,
                    primary key (id) )"""
            cursor.execute(sql)
            self.bd_conexion.commit()

    def getUser(self,usuario,contraseña):
         with self.bd_conexion.cursor() as cursor:
            sql = """SELECT nombre,correo,crearEvento,programacion,inscripciones,configuracion,tickets from Usuarios where usuario = %s and contraseña =  %s  """
            cursor.execute(sql,(usuario,contraseña,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            if resultado:
                return resultado  
            

            
         
