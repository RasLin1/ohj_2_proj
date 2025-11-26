from .entities import Entity
from ..db_classes.player_queries import create_player, move_player


class Player(Entity):
    def __init__(self, name, airport):
        super().__init__(name, airport)
        self.id = create_player(name, airport['airport_icao'])
        self.fuel = 100
        self.money  = 100
        self.max_hp = 100
        self.hp = 100
    
    def current_location(self):
        print(f'Player name: {self.name} | Location code: {self.location} | Id: {self.id}')
    
    def move_player(self, airport, distance):
        if airport == False:
            return False
        else:
            fuel_consumed = self.fuel - distance/100
            move = move_player(self.id, airport['airport_icao'], fuel_consumed)
            if move:
                self.fuel = fuel_consumed
                self.location = airport['airport_icao']
                self.location_name = airport['a_name']
                self.cordinates = (airport['lat'], airport['lon'])
            else:
                return False
            return True