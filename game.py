from classes.entity_classes.enemies import Enemy
from classes.entity_classes.player import Player
from classes.db_classes.airport_queries import select_random_airport_location, select_specific_airport, select_all_airports
from classes.db_classes.event_queries import select_random_event, select_specific_event
from functions.game_functions import probe_interaction, select_closest_airports, current_distance
import random
from flask import Flask, request, json

app = Flask(__name__)

# MUOKATTU J: tarvitaan html-tiedostojen näyttämiseen Flaskilla
from flask import send_from_directory
import os

# MUOKATTU J: määritetään polku web_pages-kansioon
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# MUOKATTU J: sallitaan html-tiedostojen tarjoilu selaimelle
@app.route('/web_pages/<path:filename>')
def serve_web_pages(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'web_pages'), filename)


GAME_STATE = {}

@app.route("/mh_game/startGame")
def startGame():
    player_name = request.args.get("name", "Anonymous")
    monster_amount = 3
    player = Player(player_name ,select_random_airport_location())
    enemies = [Enemy(select_random_airport_location(), player.id) for i in range(monster_amount)]
    GAME_STATE[player.id] =  {
        "player": player,
        "enemies": enemies,
        "round": 1
    }
    return json.dumps({"player_id": player.id,"player": player.__dict__})

@app.route("/mh_game/selectAllAirports")
def selectAllAirports():
    airports = select_all_airports()
    return json.dumps(airports)

@app.route("/mh_game/movePlayer")
def movePlayer():
    player_id = request.args.get("pid")
    if not player_id or player_id not in GAME_STATE:
        return json.dumps({"Error": "Missing or invalid id"})
    player = GAME_STATE[player_id]["player"]
    location = request.args.get("location", player.location)
    try:
        target_airport = select_specific_airport(location)
        player.move_player(target_airport, current_distance(player.cordinates, (target_airport['lat'], target_airport['lon'])))
        response = {
            "player": player.__dict__,
            "target_airport": target_airport
        }
    except TypeError:
        target_airport = select_specific_airport(player.location)
        response = {
            "player": player.__dict__,
            "target_airport": target_airport
        }
    return json.dumps(response)

@app.route("/mh_game/moveEnemies")
def moveEnemies():
    player_id = request.args.get("pid")
    if not player_id or player_id not in GAME_STATE:
        return json.dumps({"Error": "Missing or invalid id"})
    decision_list = []
    for x in GAME_STATE[player_id]["enemies"]:
        try:
            decision = x.move_decision()
            #Starts a close move
            if decision == 1:
                target = select_closest_airports(10, x.cordinates)[random.randint(0, 9)]
                x.move_enemy(target)
                response = {
                    "enemy": x.id,
                    "decision": "Close move",
                    "target": target["airport_icao"]
                }
                decision_list.append(response)
            #Starts a far away move
            elif decision == 2:
                #Should avoid an infinite loop
                airport_found = False
                attempts = 0
                while not airport_found and attempts < 500:
                    rand_airport = select_random_airport_location()
                    dist = float(current_distance(x.cordinates, (rand_airport['lat'], rand_airport['lon'])))
                    if 500.00<dist<2000.00:
                        airport_found = x.move_enemy(rand_airport)
                    attempts += 1
                if not airport_found:
                    raise Exception("No valid airport found for far move")
                response = {
                    "enemy": x.id,
                    "decision": "Far move",
                    "target": rand_airport["airport_icao"]
                }
                decision_list.append(response)
            #No movement
            else:
                response = {
                    "enemy": x.id,
                    "decision": "No move",
                    "target": "No target"
                }
                decision_list.append(response)

        except Exception as e:
            #Should work as an error log
            print("ERROR while moving enemy:", e)
            response = {
                "enemy": x.id,
                "decision": "Error",
                "error": str(e)
            }
            decision_list.append(response)
    return json.dumps(decision_list)

#Gets rand event from db and returns it's id and description
@app.route("/mh_game/getRandomEvent")
def getRandomEvent():
    try:
        event = select_random_event()
        response = {
            "id": event["event_id"],
            "description": event["event_description"],
        }
    #Should run if event is false
    except ValueError:
        response = {
            "error": "Failed retrieval of random event"
        }
    return json.dumps(response)

#Checks given answer to the correct from db, updates player value based on reward and finally returns the result, player and event reward if correct and only result and correct answer if incorrect
@app.route("/mh_game/checkEventAnswer")
def checkEventAnswer():
    #Lots of error handling and requesting args
    player_id = request.args.get("pid")
    if not player_id or player_id not in GAME_STATE:
        return json.dumps({"Error": "Missing or invalid player id"})
    event_id = request.args.get("eid")
    if not event_id:
        return json.dumps({"Error": "Missing event id"})
    user_answer = request.args.get("answer")
    if not user_answer:
        return json.dumps({"Error": "Missing user answer"})
    event = select_specific_event(event_id)
    if not event:
        return json.dumps({"Error": "Failed retrival of event"})
    #Starts if answer is correct
    elif event["event_answer"] == user_answer:
        #Gets the player
        player = GAME_STATE[player_id]["player"]
        #Updates the appropriate value for object and in db
        player.update_other_value(event["event_reward_type"], event["event_reward_value"])
        #Self explanatory response
        response = {
            "result": True,
            "player": player.__dict__,
            "reward_type": event["event_reward_type"],
            "reward_value": event["event_reward_value"]
        }
    #Starts if the answer is incorrect
    else:
        response = {
            "result": False,
            "correct_answer": event["event_answer"]
        }
    return json.dumps(response)


"""
    while allow_game:
        #The players turn starts here 
        #Asks the player for their action
        round_action = input("Kirjoita 'S' jos haluat siirtää paikkaa | Kirjoita 'L' jos haluat levätä: ").upper()
        #Starts the procedure for movement
        if round_action == 'S':
            #Retrieves the closest airport, amount determined by the first value
            closest_airports = select_closest_airports(10, player.cordinates)
            for x in closest_airports:
                print(f'Nimi: {x["a_name"]} | ICAO-koodi: {x["airport_icao"]} | Distance: {x["distance"]}')
            target_airport = select_specific_airport(input("Anna lentokentän icao-koodi jonne haluat siirtyä: ").upper())
            #Updates the players location both in db and the objective
            player.move_player(target_airport, player.fuel - float(current_distance(player.cordinates, (target_airport['lat'], target_airport['lon']))))
        if round_action == 'L':
            event_chance = random.randint(1, 3)
            if event_chance == 3:
                event = select_random_event()
                
        for x in enemies:
            print("DEBUG: enemy movement starting")
            decision = x.move_decision()
            print(f"DEBUG: enemy movement decision is {decision}")
            if decision == 1:
                target = select_closest_airports(10, x.cordinates)[random.randint(0, 9)]
                print(target)
                x.move_enemy(target)
            elif decision == 2:
                airport_found = False
                while airport_found == False:
                    rand_airport = select_random_airport_location()
                    dist = float(current_distance(x.cordinates, (rand_airport['lat'], rand_airport['lon'])))
                    if 500.00<dist<2000.00:
                        airport_found = x.move_enemy(rand_airport)
                        x.print_data()
        else:
            print("Move invalid input")
        """

        






if __name__ == '__main__':
    app.run(debug = True, use_reloader = True, host='127.0.0.1', port=3000)