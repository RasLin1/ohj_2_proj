'use strict';

const move = document.getElementById('move');
const items = document.getElementById('items');
const rest = document.getElementById('rest');
const fight = document.getElementById('fight');
const item_list = document.getElementById('item_list');
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
        <b>${ap.airport_icao}</b><br>${ap.a_name}`)
    });
  }
  catch (error) {
    console.error("Failed to load airports:", error)
  }
};

move.addEventListener('click', function() {
  //add movement selection functionality
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