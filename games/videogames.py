import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql, extras

# Load environment variables from the '.env' file in the current directory
load_dotenv()

def connect_db():
    """Attempts to establish a connection with the database and returns the connection."""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST")
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_record(conn, table, data):
    """Inserts a new record into the database."""
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
        sql.Identifier(table),
        sql.SQL(keys),
        sql.SQL(values)
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, list(data.values()))
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error inserting record: {e}")
        conn.rollback()

def read_record(conn, table, criteria):
    """Gets records from the database based on a criterion."""
    where_clause = sql.SQL(' AND ').join([sql.SQL("{} = %s").format(sql.Identifier(k)) for k in criteria])
    query = sql.SQL("SELECT * FROM {} WHERE {}").format(sql.Identifier(table), where_clause)
    try:
        with conn.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute(query, list(criteria.values()))
            result = cursor.fetchall()
        return result
    except psycopg2.Error as e:
        print(f"Error reading records: {e}")
        return []

def update_record(conn, table, data, criteria):
    """Updates records in the database based on a criterion."""
    set_clause = sql.SQL(', ').join([sql.SQL("{} = %s").format(sql.Identifier(k)) for k in data])
    where_clause = sql.SQL(' AND ').join([sql.SQL("{} = %s").format(sql.Identifier(k)) for k in criteria])
    query = sql.SQL("UPDATE {} SET {} WHERE {}").format(sql.Identifier(table), set_clause, where_clause)
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, list(data.values()) + list(criteria.values()))
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error updating record: {e}")
        conn.rollback()

def delete_record(conn, table, criteria):
    """Deletes records from the database based on a criterion."""
    where_clause = sql.SQL(' AND ').join([sql.SQL("{} = %s").format(sql.Identifier(k)) for k in criteria])
    query = sql.SQL("DELETE FROM {} WHERE {}").format(sql.Identifier(table), where_clause)
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, list(criteria.values()))
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error deleting record: {e}")
        conn.rollback()

if __name__ == "__main__":

    # CREATE
    videogames = {
        "name": "Mario Kart",
        "genre": "Sport",
        "platform": "DS",
        "release_year": 2007
    }

    conn = connect_db()
    if conn is not None:
        try:
            create_record(conn, 'videojuegos', videogames)
            print("Video game inserted successfully into the database.")
        except Exception as e:
            print(f"Error inserting video game: {e}")
        finally:
            conn.close()

    # READ
    # conn = connect_db()
    # if conn is not None:
    #     try:
    #         # Criterion to identify the video game to read
    #         criteria = {"name": "Resident Evil Village"}
            
    #         # Reads the video game based on the criterion
    #         result = read_record(conn, 'video_games', criteria)
    #         if result:
    #             print("Video Game Information:")
    #             for row in result:
    #                 print(f"Name: {row['name']}")
    #                 print(f"Genre: {row['genre']}")
    #                 print(f"Platform: {row['platform']}")
    #                 print(f"Release Year: {row['release_year']}")
    #         else:
    #             print("Video game not found in the database.")
    #     except Exception as e:
    #         print(f"Error reading video game: {e}")
    #     finally:
    #         # Closes the connection to the database
    #         conn.close()


    # UPDATE
    # conn = connect_db()
    # if conn is not None:
    #     try:
    #         # Criterion to identify the video game to update
    #         criteria = {"name": "Resident Evil Village"}
            
    #         # New data to update the video game
    #         new_data = {
    #             "genre": "Adventure, Action, Horror, Survival Horror",
    #             "platform": "PlayStation 5",
    #             "release_year": 2021
    #         }
            
    #         # Updates the video game based on the criterion and the new data
    #        
    # Updates the video game based on the criterion and the new data
    #         update_record(conn, 'video_games', new_data, criteria)
    #         print("Video game updated successfully in the database.")
    #     except Exception as e:
    #         print(f"Error updating video game: {e}")
    #     finally:
    #         # Closes the connection to the database
    #         conn.close()
    
    # DELETE
    # conn = connect_db()
    # if conn is not None:
    #     try:
    #         # Criterion to identify the video game to delete
    #         criteria = {"name": "Metal Gear"}
            
    #         # Deletes the video game based on the criterion
    #         delete_record(conn, 'videojuegos', criteria)
    #         print("Video game deleted successfully from the database.")
    #     except Exception as e:
    #         print(f"Error deleting video game: {e}")
    #     finally:
    #         # Closes the connection to the database
    #         conn.close()








    

    




