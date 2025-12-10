from .entities import Entity
from ..db_classes.enemy_queries import create_game_creature, select_specific_creature, move_creature, update_creature_health, update_creature_captured_status
import random

class Enemy(Entity):
    def __init__(self, airport, player_id):
        c = create_game_creature(airport['airport_icao'], player_id)
        super().__init__(c["name"], airport)
        self.id = c["id"]
        self.dmg = c["damage"]
        self.hp = c["health"]
        self.max_hp = c["health"]
        self.captured = False
    
    def print_data(self):
        print(f'Enemy name: {self.name} | Location code: {self.location} | ID: {self.id} | HP: {self.hp} | DMG: {self.dmg}')
    
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
                self.cordinates = airport['cordinates']
                print("DEBUG: Movement success")
                return True
            else:
                return False
    
    def update_health(self, dmg):
        self.hp = self.hp - dmg
        change = update_creature_health(self.id, dmg)
        if change:
            return True
        else:
            return False
    
    def update_status(self, status_change):
        self.captured = update_creature_captured_status(self.id, status_change)
        return self.captured