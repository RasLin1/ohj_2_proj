from classes.entity_classes.enemies import Enemy
from classes.entity_classes.player import Player
from classes.db_classes.airport_queries import select_random_airport_location, select_specific_airport, select_all_airports
from classes.db_classes.event_queries import select_random_event
from functions.game_functions import probe_interaction, select_closest_airports, current_distance
import random
from flask import Flask, request, json

app = Flask(__name__)
@app.route("/mh_game")

def play():
    player_name = request.args.get("name", "Anonymous")
    round = 1
    monster_amount = 3
    allow_game = True
<<<<<<< HEAD
    player = Player(player_name ,select_random_airport_location())
=======
    player = Player(player_name, select_random_airport_location())
>>>>>>> 05ae4333157aad4559ac62347550f10a7445a38f
    enemies = []
    dict_enemies = []
    for x in range(monster_amount):
        enemy = Enemy(f'Ent{x}', select_random_airport_location(), player.id)
        enemy.print_data()
        enemies.append(enemy)
<<<<<<< HEAD
    return json.dumps(player.__dict__)


"""
=======
    response = {
        "Player": player.__dict__
    }
    return json.dumps(response)
>>>>>>> 05ae4333157aad4559ac62347550f10a7445a38f
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
        
<<<<<<< HEAD
"""

        






if __name__ == '__main__':
=======

if __name__ == "__main__":
>>>>>>> 05ae4333157aad4559ac62347550f10a7445a38f
    app.run(debug=True)