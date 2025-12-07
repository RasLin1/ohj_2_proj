import json

from classes.db_classes.enemy_queries import select_specific_creature
from classes.db_classes.player_queries import select_specific_player

from classes.entity_classes.player import Player
from classes.entity_classes.enemies import Enemy
from flask import Flask
import random

#
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

    if enemy.hp<=0:

        return True


    else:

       capture_chance = 60-(enemy.hp+2








                         )/2
       random_value = random.randint(1,100)

       if random_value<=capture_chance:

          #capture sucess
          return True

    #idea on että tän booli mukaan päätetään napataanko hirviön
       else:
          return False



def items(player):

    if player.equiped_list[0]==0:
        player.equiped_list.append(player.inventory_list[0])
        player.dmg = player.dmg + player.equiped_list[0].dmg
        return json.dumps(player.dmg)


    else:
        player.dmg -= player.equiped_list[0].dmg
        player.equiped_list.insert(0,player.inventory_list[0])
        player.dmg += player.equiped_list[0].dmg

        return json.dumps(player.dmg)






def run(player,enemy):
    running_away_chance = player.hp/1.2 - enemy.hp/1.5
    random_value_two = random.randint(1,100)
    if random_value_two<=running_away_chance:

        return True
    else:
        return False








if __name__ == '__main__':
    app.run(debug=True)