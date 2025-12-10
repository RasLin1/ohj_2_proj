from .entities import Entity
from ..db_classes.player_queries import create_player, move_player, update_player_health, update_player_value
from ..db_classes.item_queries import assign_item


class Player(Entity):
    def __init__(self, name, airport):
        super().__init__(name, airport)
        self.id = create_player(name, airport['airport_icao'])
        self.fuel = 100
        self.money  = 100
        self.max_hp = 100
        self.hp = 100
        self.dmg = 10
        self.equipped_list = []
        self.inventory_list=[]

    
    def current_location(self):
        print(f'Player name: {self.name} | Location code: {self.location} | ID: {self.id} | HP: {self.hp} | DMG: {self.dmg}')
    
    def move_player(self, airport, distance):
        if airport == False:
            return False
        else:
            distance = float(distance)
            self.fuel = float(self.fuel)
            new_fuel = self.fuel - distance/100
            move = move_player(self.id, airport['airport_icao'], new_fuel)
            if move:
                self.fuel = new_fuel
                self.location = airport['airport_icao']
                self.location_name = airport['a_name']
                self.cordinates = (airport['lat'], airport['lon'])
            else:
                print(f"Failed DB update for player {self.id} to {airport['airport_icao']}")
                return False
            return True
        
    def update_items(self, item):
        db_success = assign_item(self.id, item["item_id"])
        if db_success:
            self.inventory_list.append(item)
            return True
        else:
            return False
        
    def equip_item(self, item):
        if item not in self.inventory_list:
            return False
        self.equipped_list.append(item)
        return True
    
    def destroy_item(self, item):
        if item not in self.inventory_list or item not in self.equipped_list:
            return False
        if item in self.inventory_list:
            self.inventory_list.remove(item)
        if item in self.equipped_list:
            self.equipped_list.remove(item)

    
    def update_health(self, change, positive):
        change = int(change)
        result = self.hp + change
        if positive and self.max_hp > result:
            self.hp = self.hp + change
        elif positive and self.max_hp <= result:
            self.hp = self.max_hp
        else:
            self.hp = self.hp - change
        change = update_player_health(self.id, change, positive)
        if change:
            return True
        else:
            return False
        
    def update_other_value(self, val, type, positive):
        if type == "fuel":
            if positive:
                self.fuel = self.fuel + int(val)
            else:
                self.fuel = self.fuel - int(val)
            change = update_player_value(type, self.fuel, self.id)
        elif type == "money":
            if positive:
                self.money = self.money + int(val)
            else:
                self.money = self.money - int(val)
            change = update_player_value(type, self.fuel, self.id)
        if change:
            return True
        else: 
            return False
        

