'use strict';

//MUOKATTU J: estetään pelin avaaminen ilman main menua
window.addEventListener('DOMContentLoaded', () => {
  const playerId = localStorage.getItem('player_id')

  if (!playerId) {
    window.location.href = '/web_pages/main_menu/main_menu.html';
    return;
  }

  console.log('Game started with player ID:', playerId);
});

// Vanha rakenne alkaa tästä
const move = document.getElementById('move');
const items = document.getElementById('items');
const rest = document.getElementById('rest');
const fight = document.getElementById('fight');
const item_list = document.getElementById('item_list');
const x = document.querySelector('span');
//MUOKATTU J: portti muutettu 5000 → 3000, jotta se toimii nykyisen game.py:n kanssa
// ALKUPERÄINEN KOODI :const gameApiLink = 'http://127.0.0.1:5000/mh_game';
const gameApiLink = 'http://127.0.0.1:3000/mh_game';



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