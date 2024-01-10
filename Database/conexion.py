import mysql.connector

def conexion():
    bd_conexion = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '1234',
            database = 'eventos',
            port = '3306'
    )
    print("Database is conected")
    return bd_conexion

