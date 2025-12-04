from creatures import update_entity_health
from db import select_specific_creature, select_specific_player
import random

def combat(player_id, creature_id):
    active_combat = True
    static_enemy = select_specific_creature(creature_id)

    while active_combat:
        player = select_specific_player(player_id)
        enemy = select_specific_creature(creature_id)
        print(f"Pelaajan arvot ovat HP:{player["current_health"]} | DMG:{player["damage"]}")
        print(f"Vastustajan arvot ovat HP:{enemy["health"]} | DMG:{enemy["damage"]}")
        if player["current_health"] > 0 and enemy["health"]>0:
            player_action = input("Kirjoita 'H' niin hyökkäät | 'S' niin yrität siepata hirviön").upper()
            if player_action == "H":
                attack_success = update_entity_health(creature_id, -player["damage"], 2)
                if attack_success == True:
                    print(f"{player["player_name"]} teki {player["damage"]} DMG {enemy["name"]} vastaan")
            if player_action == "S":
                if enemy["health"] > static_enemy["health"]/2:
                    chance = random.randint(1, 4)
                    if chance == 4:
                        print("Capture success")
                        return True
                    else:
                        print("Capture failed")
                else:
                    chance = random.randint(1, 2)
                    if chance == 2:
                        print("Capture success")
                    else:
                        print("Capture failed")
            enemy_attack = update_entity_health(player_id, -enemy["damage"], 1)
            if enemy_attack == True:
                    print(f"{enemy["name"]} teki {enemy["damage"]} DMG {player["player_name"]} vastaan")
        elif enemy["health"] <= 0:
            print(f"{player["name"]} voitti!")
            return True
        elif player["health"] <= 0:
            print(f"{player["name"]} hävisi")

    