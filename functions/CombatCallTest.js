'use strict'

import  battle from "battle"




dataSendingTest
async function CombatStart(){


  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/combat/0,0')
    const statsData = await response.json()
    monster_name.innerText= statsData.enemy_stats.name
    monster_hp.innerText = statsData.enemy_stats.health
    player_name.innerText = statsData.player_stats.name
    player_hp.innerText = statsData.player_stats.health



  }catch (error){

    console.log(error)
  }

}