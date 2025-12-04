from classes.entity_classes.enemies import Enemy
from classes.entity_classes.player import Player
from classes.db_classes.airport_queries import select_random_airport_location, select_specific_airport, select_all_airports
from classes.db_classes.event_queries import select_random_event
from functions.game_functions import probe_interaction, select_closest_airports, current_distance
import random
from flask import Flask, request, url_for,jsonify
import json

app = Flask(__name__)
@app.route('/play/')
def play():
    static = url_for('static',filename ='Test.html')
    round = 1
    monster_amount = 3
    allow_game = True
    player = "Jesse"
    enemies = []

    # data =  request.get.json()
    for x in range(monster_amount):
        enemy = Enemy(f'Ent{x}', select_random_airport_location(), player.id)
        enemy_data =  json.dumps(enemy.__dict__)
        enemies.append(enemy)
        venemy = {"Enemy": enemy_data}
        return venemy
 # render_template requires the html file in directory marked as template directory and language settings to be set html
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
            x_vastaus = {
                "Airport":x
            }
            return x_vastaus
        if round_action == 'L':
            event_chance = random.randint(1, 3)
            if event_chance == 3:
                event = select_random_event()
                
        for x in enemies:
            print("DEBUG: enemy movement starting")
            enemy_move = f"DEBUG: enemy movement starting"
            vastaus_enemy_move = {
                "Move": enemy_move
            }
            decision = x.move_decision()
            print(f"DEBUG: enemy movement decision is {decision}")
            decision_v = f"DEBUG : enemy movement decision is {decision}"
            vastaus_decision = {
                "Decision": decision_v
            }

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
            return vastaus_enemy_move,vastaus_decision

        else:
            wrong_move =f"Move invalid input"

            move_v = {
                "Invalid" : wrong_move
            }
            return move_v

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)