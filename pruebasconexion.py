#importarmos pymysql
import pymysql

#creamos la conexion
conexion = pymysql.connect(
    host='localhost',
    user='root', 
    password='', 
    db='sakila')

try:
    with conexion.cursor() as cursor:
        #creamos la consulta 
        #consulta = "SELECT * FROM actor"
        #insertar datos
        consulta = "INSERT INTO actor(first_name,last_name) VALUES('Juan','Perez')"
        #ejecutamos la consulta 
        cursor.execute(consulta)
        #obtenemos los resultados
        resultados = cursor.fetchall()
        #recorremos los resultados
        for fila in resultados:
            print(fila)
except Exception as e:
    print("Ocurrió un error al consultar: ", e) 
finally:    
    conexion.close()
    print("Conexión cerrada")

                        