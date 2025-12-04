'use strict';

const move = document.getElementById('move');
const items = document.getElementById('items');
const rest = document.getElementById('rest');
const fight = document.getElementById('fight');
const item_list = document.getElementById('item_list');
const x = document.getElementById('main_gameX');
const battle = document.getElementById('battle');
const battle_screen = document.getElementById('battle_screen');
const monster_name = document.getElementById('monster_name');
const monster_hp = document.getElementById('monster_hp_percentage');
const player_name = document.getElementById('player_name');
const player_hp = document.getElementById('player_hp_percentage');
const attack = document.getElementById('attack');
const item_battle = document.getElementById('item_battle');
const capture = document.getElementById('capture');
const runaway = document.getElementById('run');
const item_list_battle = document.getElementById('item_list_battle');
const battle_x = document.getElementById('in_battleX');
const li = document.querySelector('li');
const quit = document.getElementById('quit');

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
  //add a check to see if it is possible to fight
  let start_fight = confirm('Are you sure you want to fight?');
  if (start_fight === true) {
    battle.showModal();
  }
});

attack.addEventListener('click', function() {
  //add attack functionality
});

item_battle.addEventListener('click', function() {
  item_list_battle.showModal();
});

capture.addEventListener('click', function() {
  //add capture functionality
});

runaway.addEventListener('click', function() {
  //add a check on if running is a success
  battle.close();
});

battle_x.addEventListener('click', function() {
  item_list_battle.close();
});

li.addEventListener('click', function() {
  //add item usage functionality
});

quit.addEventListener('click', function() {
  let quit_game = confirm('Are you sure you want to quit?');
  if (quit_game === true) {
    //add save functionality?
    window.location.href = '../main_menu/main_menu.html';
  } else {
    alert('Yay! Happy gaming <3');
  }
});