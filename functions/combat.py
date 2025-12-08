import json

from classes.db_classes.enemy_queries import select_specific_creature, update_creature_captured_status
from classes.db_classes.player_queries import select_specific_player

from classes.entity_classes.player import Player
from classes.entity_classes.enemies import Enemy
from flask import Flask
import random

#
app = Flask(__name__)

@app.route("/mh_game/combat")
def combat_start(player,enemy):

  p_stats = select_specific_player(player)
  e_stats = select_specific_creature(enemy)

  if p_stats["location"]==e_stats["location"] :
      response = {
          "player_stats": p_stats,
          "enemy_stats": e_stats
      }


      return json.dumps(response)

  else:
        return False

@app.route("/mh_game/attack")
def attack(player,enemy):
    monster_health = enemy.update_health(player.dmg)





    return json.dumps(monster_health)
@app.route("/mh_game/monsterAttack")
def monster_attack(player,enemy):
    player_health = player.update_health(enemy.dmg)


    return json.dumps(player_health)

@app.route("/mh_game/capture")
def capture(player,enemy):

    if enemy.hp<=0:

        captured = update_creature_captured_status(enemy.id, True)
        return captured


    else:

       capture_chance = 60-(enemy.hp+2








                         )/2
       random_value = random.randint(1,100)

       if random_value<=capture_chance:

          #capture sucess
          captured = update_creature_captured_status(enemy.id, True)
          return captured

    #idea on että tän booli mukaan päätetään napataanko hirviön
       else:
          return False


@app.route("/mh_game/items")
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





@app.route("/mh_game/run")
def run(player,enemy):
    running_away_chance = player.hp/1.2 - enemy.hp/1.5
    random_value_two = random.randint(1,100)
    if random_value_two<=running_away_chance:

        return True
    else:
        return False








if __name__ == '__main__':
    app.run(debug=True, use_reloader = True, host='127.0.0.1', port=3000)