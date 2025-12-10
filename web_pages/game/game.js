'use strict';

const shop = document.getElementById('shop');
const shopX = document.getElementById('shopX')
const items = document.getElementById('items');
const rest = document.getElementById('rest');
const fight = document.getElementById('fight');
const item_list = document.getElementById('item_list');
const hp = document.getElementById('hp');
const fuel = document.getElementById('fuel');
const money = document.getElementById('money');
const captured = document.getElementById('captured');
const turns = document.getAnimations('turns');
const x = document.querySelector('span');
const gameApiLink = 'http://127.0.0.1:3000/mh_game';
const map = L.map('map').setView([51.505, -0.09], 13);
const music = document.getElementById('main_music');
const battle_music = document.getElementById('battle_music')

music.volume = 0.2;
music.play();

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

async function startGame() {
  const name = sessionStorage.getItem('player_name');
  const response = await fetch(
      `${gameApiLink}/startGame?name=${encodeURIComponent(name)}`);
  const gameData = await response.json();
  hp.textContent = gameData.player.hp;
  fuel.textContent = gameData.player.fuel;
  money.textContent = gameData.player.money;
  captured.textContent = 0;
  turns.textContent = gameData.turns;
  map.setView(gameData.player.cordinates, 13);
  sessionStorage.setItem('player_id', gameData.player_id);
  console.log('Game started: ', gameData);
  loadAirports();
}

//Loads all airports
async function loadAirports() {
  try {
    const response = await fetch(`${gameApiLink}/selectAllAirports`);
    const airports = await response.json();

    airports.forEach(ap => {
      if (!ap.lat || !ap.lon)
        return;
      const marker = L.marker([ap.lat, ap.lon]).addTo(map);
      marker.bindPopup(`
        <b>${ap.airport_icao}</b><br>${ap.a_name}<br><button class="move-btn" data-icao="${ap.airport_icao}">Move</button>`,
      );
    });
  } catch (error) {
    console.error('Failed to load airports:', error);
  }
};

async function movePlayer(icao) {
  const id = sessionStorage.getItem('player_id');
  const response = await fetch(
      `${gameApiLink}/movePlayer?pid=${id}&location=${icao}`);
  const result = await response.json();
  console.log('Player moved: ', result);
  turns.textContent = result.turns;
  fuel.textContent = result.player.fuel;
  const cords = result.player.cordinates;
  map.setView(cords, 13);
}

async function healPlayer(change) {
  const id = sessionStorage.getItem('player_id');
  const response = await fetch(
      `${gameApiLink}/healPlayer?pid=${id}&change=${change}`);
  const result = await response.json();
  console.log('Player healed: ', result.player.hp, 'Success:', result.result);
  hp.textContent = result.player.hp;
}

async function moveEnemies() {
  const id = sessionStorage.getItem('player_id');
  const response = await fetch(`${gameApiLink}/moveEnemies?pid=${id}`);
  const result = await response.json();
  console.log('Raw enemy movement response: ', result);
}

async function checkDistance() {
  const id = sessionStorage.getItem('player_id');
  const response = await fetch(`${gameApiLink}/enemyDistances?pid=${id}`);
  const data = await response.json();
  console.log('Distance data:', data);
  d_list.innerHTML = '';
  for (let enemy of data) { //loop that creates articles for the shows
    const li = document.createElement('li');
    li.textContent = `Enemy ${enemy.enemy}: ${enemy.distance} km away`;
    d_list.append(li);
  }
}

async function getEvent() {
  const response = await fetch(`${gameApiLink}/getRandomEvent`);
  const data = await response.json();
  console.log('Event data:', data);
  sessionStorage.setItem('current_event_id', data.id);
  document.getElementById('event_description').innerText = data.description;
  document.getElementById('event_answer_input').value = '';
  document.getElementById('event_result').innerText = '';
  document.getElementById('event_modal').showModal();
}

document.getElementById('submit_event_answer').
    addEventListener('click', async function(event) {
      const event_id = sessionStorage.getItem('current_event_id');
      const player_id = sessionStorage.getItem('player_id');
      const answer = document.getElementById('event_answer_input').value;
      console.log('Sending pid:', player_id, 'eid:', event_id, 'answer:',
          answer);
      const response = await fetch(
          `${gameApiLink}/checkEventAnswer?pid=${player_id}&eid=${event_id}&answer=${answer}`);
      const data = await response.json();
      console.log('Answer result:', data);

      if (data.result === true) {
        document.getElementById(
            'event_result').innerText = `Correct | Reward was: ${data.reward_value} ${data.reward_type}`;
        if (data.reward_type == 'fuel') {
          fuel.textContent = data.player.fuel;
        } else if (data.reward_type == 'money') {
          money.textContent = data.player.money;
        }
      } else {
        document.getElementById(
            'event_result').innerText = `Incorrect | Answer was: ${data.correct_answer}`;
      }
    });

async function combatStart() {
  const id = sessionStorage.getItem('player_id');

  try {
    const response = await fetch(`${apiLink}/allowCombat?pid=${id}`);
    const data = await response.json();

    console.log(data);
    if (!data.result) {
      console.log('No combat allowed');
      return;
    }

    sessionStorage.setItem('enemy_id', data.enemy_id);
    document.getElementById('battle').showModal();
    music.pause()
    battle_music.volume = 0.3
    battle_music.play()

  } catch (error) {

    console.log(error);
  }

}

document.addEventListener('click', async function(event) {
  //add movement selection functionality
  if (event.target.classList.contains('move-btn')) {
    const icao = event.target.dataset.icao;
    console.log('Moving to: ', icao);
    await movePlayer(icao);
    await moveEnemies();
    await checkDistance();
    await combatStart();
  }
});

items.addEventListener('click', function() {
  item_list.showModal();
});

x.addEventListener('click', function() {
  item_list.close();
});

rest.addEventListener('click', async function() {
  //add rest selection functionality
  let rest_a_turn = confirm('Are you sure you want to rest?');
  if (rest_a_turn) {
    await healPlayer(15);
    await getEvent();
  }
});

fight.addEventListener('click', function() {
  //add a check to see if its possible to fight
  let start_fight = confirm('Are you sure you want to fight?');
  if (start_fight === true) {
    document.getElementById('battle').showModal();
    music.pause()
    battle_music.volume = 0.3
    battle_music.play()
  }
});

shop.addEventListener('click', function() {
  document.getElementById('shop_modal').showModal();
});

shopX.addEventListener('click', function(){
  document.getElementById('shop_modal').close();
})

document.getElementById('quit_battle').addEventListener('click', () => {
  document.getElementById('battle').close();
  battle_music.pause()
  music.play()
});

document.getElementById('close_event_modal').addEventListener('click', () => {
  document.getElementById('event_modal').close();
});

document.addEventListener('DOMContentLoaded', async () => {
  startGame();
  checkDistance();
});

const start = [];

async function CombatStart() {

  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/combat/114/234');
    const statsData = await response.json();

    console.log(statsData);
    if (statsData === 'False') {

      console.log(`Hirviö ei ole samassa paikka eli : ${statsData}`);

    } else {

      monster_name.innerText = statsData.enemy_stats.name;
      monster_hp.innerText = statsData.enemy_stats.health;
      player_name.innerText = statsData.player_stats.name;
      player_hp.innerText = statsData.player_stats.health;

    }

  } catch (error) {

    console.log(error);
  }

}

async function Attack() {

  const p_id = sessionStorage.getItem('player_id');

  try {
    //const response = await fetch('http://127.0.0.1:3000/mh_game/attack/active_entities.players[1]/active_entities.active_ennemies[0]')
    const response = await fetch(`${gameApiLink}/attack?pid=${p_id}`);
    const statsData = await response.json();

    console.log(statsData);

    monster_hp.innerText = statsData.enemy.hp;

  } catch (error) {

    console.log(error);
  }

}

async function MonsterAttack() {
  const p_id = sessionStorage.getItem('player_id');

  try {
    // const response = await fetch('http://127.0.0.1:3000/mh_game/monsterAttack/114/234')
    const response = await fetch(`${gameApiLink}/monsterAttack?pid=${p_id}`);
    const statsData = await response.json();

    console.log(statsData);

    player_hp.innerText = statsData.player.hp;

  } catch (error) {

    console.log(error);
  }

}

async function Capture() {
  const p_id = sessionStorage.getItem('player_id');

  try {
    //const response = await fetch('http://127.0.0.1:3000/mh_game/capture/114/234')
    const response = await fetch(`${gameApiLink}/capture?pid=${p_id}`);
    const statsData = await response.json();

    if (statsData.Captured === true) {

      console.log(`${statsData}`);

      document.getElementById('battle').close();
      battle_music.pause()
      music.play()
      alert('Monster succesfully hunted');

    } else {
      console.log('Monster has not been captured');
    }

  } catch (error) {

    console.log(error);
  }

}

async function Items() {

  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/items/114/234');
    const statsData = await response.json();

    console.log(statsData);
    // monster_name.innerText= statsData.enemy_stats.name
    //monster_hp.innerText = statsData.enemy_stats.health
    //player_name.innerText = statsData.player_stats.name
    //player_hp.innerText = statsData.player_stats.health

  } catch (error) {

    console.log(error);
  }

}

async function Run() {

  try {
    const response = await fetch('http://127.0.0.1:3000/mh_game/run/114/234');
    const statsData = await response.json();

    if (statsData === 'True') {
      //poista combat ui
      monster_name.innerText = '';
      monster_hp.innerText = '';
      player_name.innerText = '';
      player_hp.innerText = '';
      window.location.href = 'game/game.html';

    } else {

    }

  } catch (error) {

    console.log(error);
  }

}

attack();





