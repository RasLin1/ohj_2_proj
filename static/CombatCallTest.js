'use strict'

const move = document.getElementById('move');
const items = document.getElementById('items');
const rest = document.getElementById('rest');
const fight = document.getElementById('fight');
const item_list = document.getElementById('item_list');
const x = document.querySelector('span');
const gameApiLink = 'http://127.0.0.1:5000/mh_game';
const playerDamage = 0;
const monsterDamage = 0;




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





// move.addEventListener('click', function() {
//   //add movement selection functionality
// });
//
// items.addEventListener('click', function() {
//   item_list.showModal();
// });
//
// x.addEventListener('click', function() {
//   item_list.close();
// });
//
// rest.addEventListener('click', function() {
//   //add rest selection functionality
//   let rest_a_turn = confirm('Are you sure you want to rest?');
// });
//
// fight.addEventListener('click', function() {
//   add a check to see if it's possible to fight
//   let start_fight = confirm('Are you sure you want to fight?');
//   if (start_fight === true) {
//     window.location.href = 'battle/battle.html';
//   }
// });










CombatStart()
Attack()
