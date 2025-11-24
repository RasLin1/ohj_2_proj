from classes.entity_classes.enemies import Enemy
from classes.entity_classes.player import Player
from classes.db_classes.airport_queries import select_random_airport_location, select_specific_airport
from geopy.distance import geodesic

def play():
    round = 1
    monster_amount = 3
    allow_game = True
    player = Player(input('Anna pelaajan nimi: ') ,select_random_airport_location())
    enemies = []
    for x in range(monster_amount):
        enemy = Enemy(f'Ent{x}', select_random_airport_location(), player.id)
        enemies.append(enemy)
    while allow_game:
        player.current_location()
        






if __name__ == '__main__':
    play()