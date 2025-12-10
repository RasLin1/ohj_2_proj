'use strict';

const move = document.getElementById('move');
const items = document.getElementById('items');
const rest = document.getElementById('rest');
const fight = document.getElementById('fight');
const item_list = document.getElementById('item_list');
const hp = document.getElementById('hp');
const fuel = document.getElementById('fuel');
const money = document.getElementById('money');
const captured = document.getElementById('captured');
const turns = document.getElementById('turns');
const d_list = document.getElementById('distance_list');
const x = document.querySelector('span');
const gameApiLink = 'http://127.0.0.1:3000/mh_game';
const map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

async function startGame() {
  const name = sessionStorage.getItem("player_name");
  const response = await fetch(`${gameApiLink}/startGame?name=${encodeURIComponent(name)}`);
  const gameData = await response.json();
  hp.textContent = gameData.player.hp;
  fuel.textContent = gameData.player.fuel;
  money.textContent = gameData.player.money;
  captured.textContent = 0;
  turns.textContent = gameData.turns;
  map.setView(gameData.player.cordinates, 13);
  sessionStorage.setItem("player_id", gameData.player_id);
  console.log("Game started: ", gameData);
  loadAirports();
}

//Loads all airports
async function loadAirports(){
  try{
    const response = await fetch(`${gameApiLink}/selectAllAirports`);
    const airports = await response.json();

    airports.forEach(ap => {
      if (!ap.lat || !ap.lon) 
        return;
      const marker = L.marker([ap.lat, ap.lon]).addTo(map);
      marker.bindPopup(`
        <b>${ap.airport_icao}</b><br>${ap.a_name}<br><button class="move-btn" data-icao="${ap.airport_icao}">Move</button>`
      );
    });
  }
  catch (error) {
    console.error("Failed to load airports:", error);
  }
};

async function movePlayer(icao) {
  const id = sessionStorage.getItem('player_id');
  const response = await fetch(`${gameApiLink}/movePlayer?pid=${id}&location=${icao}`);
  const result = await response.json();
  console.log("Player moved: ", result);
  turns.textContent = result.turns;
  fuel.textContent = result.player.fuel;
  const cords = result.player.cordinates
  map.setView(cords, 13);
}

async function healPlayer(change) {
  const id = sessionStorage.getItem('player_id');
    const response = await fetch(`${gameApiLink}/healPlayer?pid=${id}&change=${10}`);
    const result = await response.json();
    console.log("Player healed: ", result.player.hp, "Success:", result.result);
    hp.textContent = result.player.hp;
}

async function moveEnemies() {
  const id = sessionStorage.getItem('player_id');
  const response = await fetch(`${gameApiLink}/moveEnemies?pid=${id}`);
  const result = await response.json();
  console.log("Raw enemy movement response: ", result);
}

async function checkDistance() {
  const id = sessionStorage.getItem('player_id');
  const response = await fetch(`${gameApiLink}/enemyDistances?pid=${id}`);
  const data = await response.json();
  console.log("Distance data:", data);
  d_list.innerHTML = '';
  for (let enemy of data) { //loop that creates articles for the shows
    const li = document.createElement('li');
    li.textContent = `Enemy ${enemy.enemy}: ${enemy.distance} km away`;
    d_list.append(li)
  }
}

async function combatStart(){
  const id = sessionStorage.getItem('player_id');

  try {
    const response = await fetch(`${apiLink}/allowCombat?pid=${id}`)
    const data = await response.json()

    console.log(data)
    if(!data.result) {
      console.log("No combat allowed")
      return
    }

    sessionStorage.setItem("enemy_id", data.enemy_id)
    window.location.href = "battle/battle.html"


  }catch (error){

    console.log(error)
  }

}

document.addEventListener('click', async function(event) {
  //add movement selection functionality
  if (event.target.classList.contains("move-btn")) {
    const icao = event.target.dataset.icao;
    console.log("Moving to: ", icao)
    await movePlayer(icao)
    await moveEnemies()
    await checkDistance()
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
    await healPlayer(15)

    turns.textContent = result.turns;
    fuel.textContent = result.player.fuel;
    const cords = result.player.c
  }
});

fight.addEventListener('click', function() {
  //add a check to see if its possible to fight
  let start_fight = confirm('Are you sure you want to fight?');
  if (start_fight === true) {
    window.location.href = 'battle/battle.html';
  }
});

document.addEventListener("DOMContentLoaded", async ()  => {
  startGame();
  checkDistance()
})