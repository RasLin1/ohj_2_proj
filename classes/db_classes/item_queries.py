from .connection import db_connection
import mysql.connector
import random

#Arpoo satunnaisen itemin  ja  palautta sen
def select_random_item():
    db = db_connection()
    rand_item_query = "SELECT * FROM ORDER BU RAND() item LIMIT 1"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(rand_item_query)
        query_return = cursor.fetchone()
        if query_return:
            return query_return
        else:
            print("DEBUG: Error returning random item")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()
    

#HAkee itemin id:n perusteella  ja  palautta sen
def select_specific_item(item_id):
    db = db_connection()
    specific_item_query = "SELECT * FROM item WHERE item_id = %s LIMIT 1"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(specific_item_query, (item_id, ))
        query_return = cursor.fetchone()
        if query_return:
            return query_return
        else:
            print("DEBUG: Error returning specific item")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()

def assign_item(player_id, item_id):
    db = db_connection()
    assign_item_query = f"INSERT INTO owned_items (player_id, item_id) VALUES (%s, %s)"
    try: 
        cursor = db.cursor()
        cursor.execute(assign_item_query, (player_id, item_id))
        db.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("DEBUG: Error returning specific item")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()

