import os  # Importar modulo os para acceder a las variables de entorno.
import psycopg2 # Importar psycopg2 para realizar la conexión con una base de datos.
from dotenv import load_dotenv

load_dotenv()

def conexion_db(): # Vamos a establecer una conexión con la base de datos y retornar algo....
    try:
       conexion = psycopg2.connect(
           host=os.environ.get("DB_HOST"), # environ es un objeto de tipo diccionario del modulo os
           port=os.environ.get("DB_PORT"),
           dbname=os.environ.get("DB_NAME"),
           user=os.environ.get("DB_USER"),
           password=os.environ.get("DB_PASSWORD"),
         )
       return conexion
    except psycopg2.Error as Error: # He renombrado por la palabra Error.
     print(f"Error.No ha sido posible conectarse a la base de datos: {Error}")
     print(Error)
     return None
    
conexion = conexion_db() # establecer conexion con la base de datos
if conexion is not None:
   cur = conexion.cursor() # cur te permite interactuar con la base de datos ejecutando consultas SQL y obteniendo resultados.
   insertar_registro = 'INSERT INTO videojuegos(id, nombre, genero, plataforma, año_lanzamiento) VALUES (%s, %s, %s, %s, %s)' # %s es un marcador de posición que indica donde se debe insertar el valor.
   insertar_valor = (2, "Kindom Hearts", "Aventura", "PC", 2010) # Inserto videojuego  
   cur.execute(insertar_registro, insertar_valor) # Ejecuta la conexión con la base de datos insertando el registro y el valor.
   conexion.commit() # Guarda los cambios realizados en la base de datos.
   cur.close() # Cierra el cursor que se ha utilizado para realizar consultas SQL en la base de datos.
   conexion.close() # Cierra la conexión con la base de datos.

    

    




