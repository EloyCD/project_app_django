# db_utils.py
import os                   # Importa el módulo os para interactuar con el sistema operativo
from dotenv import load_dotenv  # Importa la función load_dotenv de la librería python-dotenv
import psycopg2             # Importa el módulo psycopg2 para poder trabajar con PostgreSQL

# Carga las variables de entorno desde el archivo '.env' en el directorio actual
load_dotenv()               

def connect_db():
    # Esta función crea y retorna una nueva conexión a la base de datos PostgreSQL
    # Utiliza las variables de entorno o valores predeterminados si no están definidas
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),  # Obtiene el nombre de la base de datos del archivo .env
        user=os.getenv("DB_USER"),       # Obtiene el nombre de usuario de la base de datos del archivo .env 
        password=os.getenv("DB_PASSWORD"), # Obtiene la contraseña de la base de datos del archivo .env 
        host=os.getenv("DB_HOST")           # Obtiene el host de la base de datos del archivo .env o usa 'localhost
    )

# Este bloque se ejecuta solo si el script es el punto de entrada principal, es decir, no se importa desde otro script
if __name__ == "__main__":
    conn = connect_db()  # Establece una conexión con la base de datos y guarda la conexión en la variable conn
    # Aquí irían las operaciones con la base de datos (consultas, inserciones, actualizaciones, etc.)
    conn.close()         # Cierra la conexión a la base de datos cuando las operaciones han terminado

def create_record(conn, table, data):
    """Inserta un nuevo registro en la base de datos."""
    keys = ', '.join(data.keys())  # Combina las llaves del diccionario 'data' en una cadena separada por comas.
    values = ', '.join(['%s'] * len(data))  # Crea una cadena de placeholders '%s' para los valores, basada en el número de elementos en 'data'.
    sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"  # Construye la sentencia SQL de inserción.
    with conn.cursor() as cursor:  # Abre un nuevo cursor para ejecutar operaciones en la base de datos.
        cursor.execute(sql, list(data.values()))  # Ejecuta la sentencia SQL con los valores proporcionados.
    conn.commit()  # Confirma (commit) la transacción para asegurar que los cambios se guarden en la base de datos.

def read_record(conn, table, criteria):
    """Obtiene registros de la base de datos según un criterio."""
    sql = f"SELECT * FROM {table} WHERE " + ' AND '.join([f"{k}=%s" for k in criteria])  # Construye la sentencia SQL de selección basada en el criterio dado.
    with conn.cursor() as cursor:
        cursor.execute(sql, list(criteria.values()))  # Ejecuta la sentencia SQL pasando los valores del criterio.
        result = cursor.fetchall()  # Recupera todos los registros que cumplen con el criterio.
    return result  # Devuelve los registros obtenidos.


def update_record(conn, table, data, criteria):
    """Actualiza registros en la base de datos basado en un criterio."""
    set_clause = ', '.join([f"{k}=%s" for k in data])  # Construye la cláusula SET para la actualización.
    where_clause = ' AND '.join([f"{k}=%s" for k in criteria])  # Construye la cláusula WHERE para filtrar los registros a actualizar.
    sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"  # Construye la sentencia SQL de actualización.
    with conn.cursor() as cursor:
        cursor.execute(sql, list(data.values()) + list(criteria.values()))  # Ejecuta la sentencia SQL con los valores de 'data' y 'criteria'.
    conn.commit()  # Confirma la transacción.


def delete_record(conn, table, criteria):
    """Elimina registros de la base de datos basado en un criterio."""
    where_clause = ' AND '.join([f"{k}=%s" for k in criteria])  # Construye la cláusula WHERE para identificar los registros a eliminar.
    sql = f"DELETE FROM {table} WHERE {where_clause}"  # Construye la sentencia SQL de eliminación.
    with conn.cursor() as cursor:
        cursor.execute(sql, list(criteria.values()))  # Ejecuta la sentencia SQL pasando los valores del criterio.
    conn.commit()  # Confirma la transacción.
