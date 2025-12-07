import json

from classes.db_classes.enemy_queries import select_specific_creature
from classes.db_classes.player_queries import select_specific_player

from classes.entity_classes.player import Player
from classes.entity_classes.enemies import Enemy
from flask import Flask
import random

# def combat(player_id, creature_id):
#     active_combat = True
#     static_enemy = select_specific_creature(creature_id)
#
#     while active_combat:
#         player = select_specific_player(player_id)
#         enemy = select_specific_creature(creature_id)
#         print(f"Pelaajan arvot ovat HP:{player["current_health"]} | DMG:{player["damage"]}")
#         print(f"Vastustajan arvot ovat HP:{enemy["health"]} | DMG:{enemy["damage"]}")
#         if player["current_health"] > 0 and enemy["health"]>0:
#             player_action = input("Kirjoita 'H' niin hyökkäät | 'S' niin yrität siepata hirviön").upper()
#             if player_action == "H":
#                 attack_success = Player.update_health(creature_id, -player["damage"], 2)
#                 if attack_success == True:
#                     print(f"{player["player_name"]} teki {player["damage"]} DMG {enemy["name"]} vastaan")
#             if player_action == "S":
#                 if enemy["health"] > static_enemy["health"]/2:
#                     chance = random.randint(1, 4)
#                     if chance == 4:
#                         print("Capture success")
#                         return True
#                     else:
#                         print("Capture failed")
#                 else:
#                     chance = random.randint(1, 2)
#                     if chance == 2:
#                         print("Capture success")
#                     else:
#                         print("Capture failed")
#             enemy_attack = Player.update_health(player_id, -enemy["damage"], 1)
#             if enemy_attack == True:
#                     print(f"{enemy["name"]} teki {enemy["damage"]} DMG {player["player_name"]} vastaan")
#         elif enemy["health"] <= 0:
#             print(f"{player["name"]} voitti!")
#             return True
#         elif player["health"] <= 0:
#             print(f"{player["name"]} hävisi")

app = Flask(__name__)

@app.route("/combat")
def combat_start(player,enemy):
  if (player.location ==enemy.location ):
   ## pitäisi ladata tai siirtää taistelu
   #combat sivulle ja jotenkin enablata combat ui html elementti



    return


def attack(player,enemy):
    monster_health = enemy.update_health(player.dmg)




    return json.dumps(monster_health)

def monster_attack(player,enemy):
    player_health = player.update_health(enemy.dmg)


    return json.dumps(player_health)

def capture(player,enemy):
    capture_chance = 60-(enemy.hp+2








                         )/2
    random_value = random.randint(1,100)

    if random_value<=capture_chance:

        #capture sucess
       return True

    #idea on että tän booli mukaan päätetään napataanko hirviön
    else:
         return False



def items(player,item):

    new_damage  =  player.dmg= player.dmg + item.dmg
     #sit deletataan esine jotenkin inventorista ettei tule infinite damage loop
     # pitäisi varmaan muualle listalle , joka pitää aina yhden arvon joka olii viimeisin esine
    # sit kun vaihdetaan esinettä periaatteessa poistetaan pelaaja esine palautetaan alkuperäiseen arvoon ja asetaan arvon paikalle uusi


    return json.dumps(new_damage)

def run(player,enemy):
    running_away_chance = player.hp/1.2 - enemy.hp/1.5
    random_value_two = random.randint(1,100)
    if random_value_two<=running_away_chance:

        return True
    else:
        return False








if __name__ == '__main__':
    app.run(debug=True)