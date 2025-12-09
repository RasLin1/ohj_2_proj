from .connection import db_connection
import mysql.connector

#Arpoo satunnaisen lentokentän  ja  palautta sen
def select_random_airport_location():
    db = db_connection()
    airport_rand_query = "SELECT airport.name AS a_name, airport.ident AS airport_icao, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS c_name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE airport.type = 'large_airport' AND airport.continent =  'EU' ORDER BY RAND() LIMIT 1"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_rand_query)
        query_return = cursor.fetchone()
        if query_return:
            return query_return
        else:
            print("DEBUG: Error returning specific airport")
            cursor.close()
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()
    

#Ottaa lentokenttä  icao koodin  inputtina  ja hakee sen  kentokentän tietokannasta. 
def select_specific_airport(icao):
    db = db_connection()
    airport_query = "SELECT airport.name AS a_name, airport.ident AS airport_icao, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS c_name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE ident = %s"
    print(f"Target icao: {icao}")
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query, (icao,))
        query_return = cursor.fetchone()
        print(query_return)
        if query_return:
           return query_return
        else:
            print("DEBUG: Error returning specific airport")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()
        

#Hakee kaikki lentokentät  tietokannasta
def select_all_airports():
    db = db_connection()
    airport_query = "SELECT airport.name AS a_name, airport.ident AS airport_icao, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS country_name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query)
        query_return = cursor.fetchall()
        if query_return:
            return query_return
        else:
            print("DEBUG: Error returning all airports list")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    finally:
        cursor.close()
        db.close()

# Hakee kaikki lentokentät tietystä maasta
def select_airports_by_country(country_name):
    db = db_connection()
    airport_query = "SELECT airport.name AS a_name, airport.ident AS airport_icao, airport.type AS airport_type, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS country_name FROM airport INNER JOIN country  ON airport.iso_country = country.iso_country WHERE country.name = %s"
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query, (country_name, ))
        query_return = cursor.fetchall()
        if query_return:
            return query_return
        else:
            print(f"Ei löytynyt lentokenttiä maalle: {country_name}")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()