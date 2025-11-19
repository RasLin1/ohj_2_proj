import mysql.connector

def db_connection():
        return mysql.connector.connect(
            host="127.0.0.1",
            port = 3306,
            database = "monster_game",
            user="monster_game",
            password="teamseven"
        )