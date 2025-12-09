'use strict';

//const game_id = localStorage.getItem('game_id')

const monster_name = document.getElementById('monster_name');
const monster_hp = document.getElementById('monster_hp_percentage');
const player_name = document.getElementById('player_name');
const player_hp = document.getElementById('player_hp_percentage');
const attack = document.getElementById('attack');
const item = document.getElementById('item');
const capture = document.getElementById('capture');
const runaway = document.getElementById('runaway');

attack.addEventListener('click', function() {
  //add attack functionality
});

item.addEventListener('click', function() {

});


async function CombatStart(){


  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/combat/114/234')
    const statsData = await response.json()

    console.log(statsData)
    if(statsData ==="False")

      console.log(`Hirviö ei ole samassa paikka eli : ${statsData}`)

    monster_name.innerText= statsData.enemy_stats.name
    monster_hp.innerText = statsData.enemy_stats.health
    player_name.innerText = statsData.player_stats.name
    player_hp.innerText = statsData.player_stats.health



  }catch (error){

    console.log(error)
  }

}

async function Attack(){


  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/attack/114/234')
    const statsData = await response.json()

    console.log(statsData)

    monster_hp.innerText -= statsData.enemy_stats.dmg





  }catch (error){

    console.log(error)
  }

}

async function MonsterAttack(){


  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/monsterAttack/114/234')
    const statsData = await response.json()

    console.log(statsData)

    player_hp.innerText -= statsData.dmg



  }catch (error){

    console.log(error)
  }

}

async function Capture(){


  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/capture/114/234')
    const statsData = await response.json()

    if(statsData.value==="False") {

      console.log(`${statsData}`)

    }
    else {

    }



  }catch (error){

    console.log(error)
  }





}

async function Items(){


  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/items/114/234')
    const statsData = await response.json()

    console.log(statsData)
   // monster_name.innerText= statsData.enemy_stats.name
    //monster_hp.innerText = statsData.enemy_stats.health
    //player_name.innerText = statsData.player_stats.name
    //player_hp.innerText = statsData.player_stats.health



  }catch (error){

    console.log(error)
  }

}


async function Run(){


  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/run/114/234')
    const statsData = await response.json()

    if(statsData==="True"){
      //poista combat ui
    monster_name.innerText= '';
    monster_hp.innerText = '';
    player_name.innerText = '';
    player_hp.innerText = '';
   window.location.href = 'game/game.html';

    }
    else {



    }



  }catch (error){

    console.log(error)
  }

}
