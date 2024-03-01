import os  # Import os module to access environment variables.
import psycopg2 # Import psycopg2 to make the connection to a database.
from dotenv import load_dotenv

load_dotenv()

def connection_db(): # Let's establish a connection with the database and return something....
    try:
       connection = psycopg2.connect(
           host=os.environ.get("DB_HOST"), # environ is an object of type dictionary of module os
           port=os.environ.get("DB_PORT"),
           dbname=os.environ.get("DB_NAME"),
           user=os.environ.get("DB_USER"),
           password=os.environ.get("DB_PASSWORD"),
         )
       return connection
    except psycopg2.Error as Error: # I have renamed by the word Error.
     print(f"It was not possible to connect to the database: {Error}")
     print(Error)
     return None
    
connection = connection_db() # establish a connection to the database
if connection is not None:
   cur = connection.cursor() # cur allows you to interact with the database by executing SQL queries and obtaining results.
   insert_record = 'INSERT INTO videojuegos(id, name, genre, platform, release_year) VALUES (%s, %s, %s, %s, %s)' # %s is a placeholder indicating where the value should be inserted.
   insert_value = (8, "Top Spin", "Sport", "PlayStation3", 2009) # Insert videogame 
   cur.execute(insert_record, insert_value) # Executes the connection to the database by inserting the record and the value.
   connection.commit() # Saves the changes made to the database.
   cur.close() # Closes the cursor that has been used to perform SQL queries on the database.
   connection.close() # Closes the connection to the database.

def create_game(id, name, genre, platform, release_year):
    print("Id:", id)
    print("Name:", name)
    print("Genre:", genre)
    print("Platform:", platform)
    print("Release_year:", release_year)

    
    connection = psycopg2.connect(
           host=os.environ.get("DB_HOST"), # environ is an object of type dictionary of module os
           port=os.environ.get("DB_PORT"),
           dbname=os.environ.get("DB_NAME"),
           user=os.environ.get("DB_USER"),
           password=os.environ.get("DB_PASSWORD"),
    )

    # Create cursor
    cur = connection.cursor()

    # Insert videogame into database 
    insert_record = 'INSERT INTO videojuegos(id, name, genre, platform, release_year) VALUES (%s, %s, %s, %s, %s)'
    insert_value = (id, name, genre, platform, release_year)
    cur.execute(insert_record, insert_value)

    # transacction ok
    connection.commit()

    # Close cursor and connect
    cur.close()
    connection.close()

def read_game(name):
    
    print("Enter the game name:", name)
    
    connection = psycopg2.connect(
           host=os.environ.get("DB_HOST"), # environ is an object of type dictionary of module os
           port=os.environ.get("DB_PORT"),
           dbname=os.environ.get("DB_NAME"),
           user=os.environ.get("DB_USER"),
           password=os.environ.get("DB_PASSWORD"),
    )

    # Create cursor
    cur = connection.cursor()

    # Insert videogame into database 
    read_record = 'SELECT * FROM videojuegos WHERE name = %s, %s'
    cur.execute(read_record, (name,))

    # transacction ok
    connection.commit()

    # Close cursor and connect
    cur.close()
    connection.close()

def update_game(id, name=None, genre=None, platform=None, release_year=None):
# In this case, we expect an id to be entered when the update function is called, we specify None since there is no value entered at first.
    
    connection = psycopg2.connect(
           host=os.environ.get("DB_HOST"),
           port=os.environ.get("DB_PORT"),
           dbname=os.environ.get("DB_NAME"),
           user=os.environ.get("DB_USER"),
           password=os.environ.get("DB_PASSWORD"),
    )
   
    cur = connection.cursor()
    update_record = "UPDATE videojuegos SET "
    update_values = [] # The corresponding value is updated in the database.

    if name:
      update_game = update_game + "nombre = '" + name + "', "
    if genre:
      update_game = update_game + "genero = '" + genre + "', "
    if platform:
      update_game = update_game + "plataforma = '" + platform + "', "
    if release_year:
      update_game = update_game + "año = '" + str(release_year) + "', "







    

    




