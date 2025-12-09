from .connection import db_connection
import mysql.connector

#Luo valitse ja luo hirviön peliä varten
def create_game_creature(location, player_id):
    db = db_connection()
    select_creature = select_random_creature()
    create_game_creature_query = f"INSERT INTO game_creatures (player_id, creature_id, creature_location, creature_current_health, creature_captured) VALUES (%s, %s, %s, %s, %s)"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(create_game_creature_query, (player_id, select_creature["creature_id"], location, select_creature["creature_max_health"], False))
        db.commit()
        creature_id = cursor.lastrowid
        creature = select_specific_creature(creature_id)
        if creature:
            return creature
        else:
            print("DEBUG: No ID returned — insert may have failed or triggered constraint.")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    finally:
        cursor.close()
        db.close()

#Hakee random hirviön
def select_random_creature():
    db = db_connection()
    random_creature_query = f"SELECT * FROM creature ORDER BY RAND() LIMIT 1"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(random_creature_query)
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

#Hakee hirviön käyttäen id arvoa"
def select_specific_creature(id):
    db = db_connection()
    specific_creature_query = f"SELECT game_creatures.id AS id, game_creatures.creature_current_health AS health, game_creatures.creature_captured AS status, creature.creature_damage AS damage, creature.creature_name AS name, creature_location AS location FROM game_creatures INNER JOIN creature ON game_creatures.creature_id = creature.creature_id WHERE game_creatures.id = %s LIMIT 1"
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

def move_creature(id, new_location):
    db = db_connection()
    move_creature_query = f"UPDATE game_creatures SET creature_location = %s WHERE id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(move_creature_query, (new_location, id))
        db.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("DEBUG: No creature updated — check creature ID or location.")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        cursor.close()
        return False
    finally:
        cursor.close()
        db.close()

def update_creature_health(id, health_change):
    db = db_connection()
    select_player_query = f"SELECT creature_current_health FROM game_creatures WHERE id = %s"
    cursor = db.cursor(dictionary=True)
    cursor.execute(select_player_query, (id, ))
    query_return = cursor.fetchone()
    new_health = query_return["creature_current_health"] + (health_change)
    update_creature_query = f"UPDATE game_creatures SET creature_current_health = %s WHERE id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(update_creature_query, (new_health, id, ))
        db.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("DEBUG: Error in updating creature health")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()

def update_creature_captured_status(id, status_change):
    db = db_connection()
    update_player_query = f"UPDATE game_creature SET creature_captured = %s WHERE id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(update_player_query, (status_change, id))
        db.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("DEBUG: Error in updating creature captured status")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()








