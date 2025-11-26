from .connection import db_connection
import mysql.connector

def create_player(name, location):
    db = db_connection()
    create_player_query = f"INSERT INTO player (player_name, player_location, fuel, money, max_health, current_health, damage, game_score, game_completed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(create_player_query, (name, location, 100, 100, 100, 100, 10, 0, False))
        db.commit()
        pid = cursor.lastrowid
        if pid:
            return pid
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    finally:
        cursor.close()
        db.close()

#Hakee pelaajan käyttäen id arvoa"
def select_specific_player(id):
    db = db_connection()
    specific_creature_query = f"SELECT * FROM player WHERE player_id = %s LIMIT 1"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(specific_creature_query, (id, ))
        query_return = cursor.fetchone()
        if query_return:
            return query_return
        else:
            print("Hirviöö ei löytynyt")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()

def move_player(id, new_location, current_fuel):
    db = db_connection()
    move_player_query = f"UPDATE player SET player_location = %s, fuel = %s WHERE player_id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(move_player_query, (new_location, current_fuel, id))
        db.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("DEBUG: No player updated — check player ID or location.")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()
    
def update_player_health(id, health_change):
    db = db_connection()
    update_player_hp_query = f"SELECT current_health FROM player WHERE player_id = %s"
    cursor = db.cursor(dictionary=True)
    cursor.execute(update_player_hp_query, (id, ))
    query_return = cursor.fetchone()
    new_health = query_return["current_health"] + (health_change)
    update_player_query = f"UPDATE player SET current_health = %s WHERE player_id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(update_player_query, (new_health, id))
        db.commit()
        if cursor.rowcount > 0:
            print(f"Players health is now {new_health}")
            return True
        else:
            print("DEBUG: Error in updating player health")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()

#Modular funktion that works for player fuel or money
def update_player_value(value_name, value_change, id):
    allowed_columns  = ["fuel", "money"]
    if value_name not in allowed_columns:
        print(f"DEBUG: Invalid column name: {value_name}")
        return False
    db = db_connection()
    select_player_query = f"SELECT {value_name} FROM player WHERE player_id = %s"
    cursor = db.cursor(dictionary=True)
    cursor.execute(select_player_query, (id, ))
    query_return = cursor.fetchone()
    new_value = query_return[f"{value_name}"] + (value_change)
    cursor =  db.cursor()
    update_player_query = f"UPDATE player SET {value_name} = %s WHERE player_id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(update_player_query, (new_value, id))
        db.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("DEBUG: Error in updating value health")
            return False
    except mysql.connector.Error as err:
        print("DEBUG: Error while updating player value")
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()