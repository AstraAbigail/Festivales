class Tickets():

    def __init__(self,bd_conexion):
        self.bd_conexion = bd_conexion
        
        with self.bd_conexion.cursor() as cursor:
            print("cursor",cursor)
            sql = """CREATE TABLE IF NOT EXISTS Tickets
                    (
                    id int auto_increment  NOT NULL,
                    cod int not null,
                    festival int not null ,
                    evento int NOT NULL,
                    fecha    date not  null,
                    categoria int not null,
                    nombre int not null,
                    sector int not null,
                    fila int not null,
                    butaca int not null,
                    precioSector decimal(7,2) not null,
                    tipoEntrada int not null,
                    precioEntrada decimal (7,2) not null,
                    cantidad int not null,
                    precioTotal decimal(7,2) not null,
                    eliminado varchar(10)not null,
                    primary key (id),
                    foreign KEY (festival) references eventos(id),
                    FOREIGN KEY (evento) REFERENCES estadios(id),
                    FOREIGN KEY (nombre) REFERENCES inscripciones(id),
                    FOREIGN KEY (sector) REFERENCES sectores(id),
                    FOREIGN KEY (tipoEntrada) REFERENCES tarifas(id)
                    )"""
            cursor.execute(sql)
            self.bd_conexion.commit()

    def tieneTickets(self,nombre,lugar): 
        with self.bd_conexion.cursor(buffered=True) as cursor:            
                sql = """ SELECT * FROM tickets  WHERE evento = %s and  festival = %s """
                cursor.execute(sql,(lugar,nombre)) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchall()
                print("Tickets MODIFICAR:",resultado)
                #self.bd_conexion.cursor.close()
                return resultado
    
    def ticketsInscripcion(self,nombre):
        with self.bd_conexion.cursor(buffered=True) as cursor:            
                sql = """ SELECT id FROM tickets  WHERE  nombre = %s """
                cursor.execute(sql,(nombre,)) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchone()
                print("Tickets INSCRIPCION:",resultado)
                return  resultado

    def ticket_Programacion(self,nombre,fecha,evento):
        with self.bd_conexion.cursor(buffered=True) as cursor:            
            sql = """ SELECT id FROM tickets  WHERE  nombre = %s and fecha = %s  and festival = %s and eliminado='No' """
            cursor.execute(sql,(nombre,fecha,evento)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchall()
            print("Tickets Programacion tiene:",resultado)
            return  resultado

    def ticket_ProgramacionEliminar(self,festival,categoria,nombre,fecha):
        with self.bd_conexion.cursor(buffered=True) as cursor:            
            sql = """ SELECT id FROM tickets  WHERE  festival = %s and categoria = %s and nombre =%s and fecha = %s and eliminado = 'No' """
            cursor.execute(sql,(festival,categoria,nombre,fecha)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchone()
            print("Tickets Eliminado:",resultado)
            return resultado
    
    
    def verificarEntradaByFilaButacaSectorFechaEvento(self,fila,butaca,sector,fecha,evento,banda):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT cod FROM tickets  WHERE  fila = %s and butaca =%s and sector =%s and fecha =%s and evento =%s and nombre = %s and eliminado = 'No' """
            cursor.execute(sql,(fila,butaca,sector,fecha,evento,banda)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchall()
            print("VERIFICACION:",resultado)
            return resultado
        
    def codigosNoUsado(self,codigo):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT cod FROM tickets  WHERE  eliminado = 'No' and cod = %s """
            cursor.execute(sql,(codigo,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchall()
            print("Codigo:",resultado)
            return resultado




    def  ingresar(self,cod,idFestival,idEvento,fecha,idCategoria,idNombre,idSector,fila,butaca,precioSector,idTipoEntrada,precioEntrada,cantidad,precioTotal,eliminado):
        with self.bd_conexion.cursor() as cursor:         
            sql = """INSERT INTO tickets(cod,festival,evento,fecha,categoria,nombre,sector,fila,butaca,precioSector,tipoEntrada,precioEntrada,cantidad,precioTotal,eliminado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql,(cod,idFestival,idEvento,fecha,idCategoria,idNombre,idSector,fila,butaca,precioSector,idTipoEntrada,precioEntrada,cantidad,precioTotal,eliminado))
            self.bd_conexion.commit()

    def showTicketsSoul(self):        
        with self.bd_conexion.cursor() as cursor:            
                sql = """ SELECT cod,fecha,sector,fila,butaca,cantidad,tipoEntrada,precioEntrada,precioSector,nombre,evento,festival FROM tickets  WHERE   eliminado = 'No' """
                cursor.execute(sql) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchall()                
                print("Tickets vendidos:",resultado)
                return resultado
    
    def selectCod_TicketByID(self,cod):
        with self.bd_conexion.cursor() as cursor:            
                sql = """ SELECT cod,id FROM tickets  WHERE   eliminado = 'No' and cod =%s """
                cursor.execute(sql,(cod,)) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchall()              
                if resultado:
                    return resultado 
    
    def ticketUpdateEliminar(self,cod):
        with self.bd_conexion.cursor() as cursor:            
                sql = """ SELECT id,festival,evento,nombre,fila,butaca,sector FROM tickets  WHERE   eliminado = 'No' and cod =%s """
                cursor.execute(sql,(cod,)) #mysql  necesita una tupla, minimamente o list o diccionario
                resultado = cursor.fetchall()              
                if resultado:
                    return resultado 
                 
    def eliminar (self,fila,butaca,id_,eliminado):
        with self.bd_conexion.cursor() as cursor:         
            sql = """UPDATE Tickets SET fila = %s, butaca = %s, eliminado = %s  WHERE id = %s"""
            cursor.execute(sql,(fila,butaca,eliminado,id_))
            self.bd_conexion.commit()  

    def pdf(self,id_pdf):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT *  FROM tickets  WHERE   eliminado = 'No' and id =%s """
            cursor.execute(sql,(id_pdf,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchall()              
            if resultado:
                return resultado  
            
    def ticketsByNameSector_Estadio(self,id_estadio,cod_sector):
         with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT id  FROM tickets  WHERE   eliminado = 'No' and  evento =%s and sector =%s """
            cursor.execute(sql,(id_estadio,cod_sector,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchall()              
            return resultado  
    
    def sectoresVendidosByestadioId(self,cod_id):
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT id  FROM tickets  WHERE   eliminado = 'No' and evento =%s """
            cursor.execute(sql,(cod_id,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchall()              
            print(resultado)
            return resultado  
        
    def ticketsVendidosByID_ESTADIO(self,id_lugar): 
        with self.bd_conexion.cursor() as cursor:            
            sql = """ SELECT id  FROM tickets  WHERE   eliminado = 'No' and evento =%s """
            cursor.execute(sql,(id_lugar,)) #mysql  necesita una tupla, minimamente o list o diccionario
            resultado = cursor.fetchall()              
            print(resultado)
            return resultado  