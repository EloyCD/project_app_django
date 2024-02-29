import os  # Importar modulo os para acceder a las variables de entorno.
import psycopg2 # Importar psycopg2 para realizar la conexión con una base de datos.

def conexion_db(): # Vamos a establecer una conexión con la base de datos y retornar algo....
    try:
       conexion = psycopg2.connect(
           db_host=os.environ.get("DB_HOST"),
           db_port=os.environ.get("DB_PORT"),
           db_name=os.environ.get("DB_NAME"),
           db_user=os.environ.get("DB_USER"),
           db_password=os.environ.get("DB_PASSWORD"),
         )
    except psycopg2.ConnectionError as Error: # He renombrado por la palabra Error.
     print(f"Error.No ha sido posible conectarse a la base de datos: {Error}")
     print(Error)
     return None
    
    



