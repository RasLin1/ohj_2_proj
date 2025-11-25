import random

class Entity():
    def __init__(self, name, airport):
        self.name = name
        self.location = airport["airport_icao"]
        self.location_name = airport["a_name"]
        self.cordinates = (airport["lat"], airport["lon"])




