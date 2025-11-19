import random

class Entity():
    def __init__(self, id, airport):
        self.id = id
        self.location = airport["airport_icao"]
        self.location_name = airport["a_name"]
        self.cordinates = (airport["lat"], airport["lon"])

class Player(Entity):
    def __init__(self, name, id, airport):
        super().__init__(name, id, airport)
        self.name = name
        self.fuel = 100
        self.money  = 100

class Enemy(Entity):
    def __init__(self, name, id, airport):
        super().__init__(name, id, airport)
