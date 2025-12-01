from .connection import db_connection
import mysql.connector
import random

#Arpoo satunnaisen tapahtuman ja palautta sen
def select_random_event():
    db = db_connection()
    event_amount_query = "SELECT COUNT(*) FROM events"
    cursor = db.cursor()
    cursor.execute(event_amount_query)
    query_return = cursor.fetchone()
    event_count = query_return[0]
    event_number = random.randint(0, (event_count - 1))
    random_event_query = f"SELECT * FROM events LIMIT 1 OFFSET %s "
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(random_event_query, (event_number,))
        query_return = cursor.fetchone()
        if query_return:
            return query_return
        else:
            print("Tapahtumaa ei löytynyt")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()