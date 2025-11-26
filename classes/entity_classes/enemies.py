from .entities import Entity
from ..db_classes.enemy_queries import create_game_creature, select_random_creature, move_creature
import random

class Enemy(Entity):
    def __init__(self, name, airport, player_id):
        super().__init__(name, airport)
        self.id = create_game_creature(name, airport['airport_icao'], player_id)
    
    def print_data(self):
        print(f'Enemy name: {self.name} | Location code: {self.location} | Id: {self.id}')
    
    def move_decision(self):
        movement_decision = random.randint(1,3)
        #returns the distance of said aiport
        if movement_decision == 3 :
            jump_distance = random.randint(1,15)
            #monster has decided to move
            if jump_distance == 15:
                return 2
            else:
                #select a random airport in the list
                return 1
        else:
            return 0
    
    def move_enemy(self, airport):
        if airport == False:
            return False
        else:
            print(airport)
            move = move_creature(self.id, airport['airport_icao'])
            if move:
                self.location = airport['airport_icao']
                self.location_name = airport['a_name']
                self.cordinates = (airport['lat'], airport['lon'])
                return True
            else:
                return False