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
  hp.textContent = gameData.player.hp
  fuel.textContent = gameData.player.fuel
  money.textContent = gameData.player.money
  map.setView(gameData.player.cordinates, 13)
  sessionStorage.setItem("player_id", gameData.player_id)
  console.log("Game started: ", gameData)
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
  const cords = result.player.cordinates
  map.setView(cords, 13);
}

document.addEventListener('click', function(event) {
  //add movement selection functionality
  if (event.target.classList.contains("move-btn")) {
    const icao = event.target.dataset.icao;
    console.log("Moving to: ", icao)
    movePlayer(icao)
  }
});

items.addEventListener('click', function() {
  item_list.showModal();
});

x.addEventListener('click', function() {
  item_list.close();
});

rest.addEventListener('click', function() {
  //add rest selection functionality
  let rest_a_turn = confirm('Are you sure you want to rest?');
});

fight.addEventListener('click', function() {
  //add a check to see if its possible to fight
  let start_fight = confirm('Are you sure you want to fight?');
  if (start_fight === true) {
    window.location.href = 'battle/battle.html';
  }
});

document.addEventListener("DOMContentLoaded", () => {
  startGame();
})