from .entities import Entity
from ..db_classes.enemy_queries import create_game_creature, select_random_creature

class Enemy(Entity):
    def __init__(self, name, airport, player_id):
        super().__init__(name, airport)
        self.id = create_game_creature(name, airport['airport_icao'], player_id)
    
    def print_data(self):
        print(f'Enemy name: {self.name} | Location code: {self.location} | Id: {self.id}')