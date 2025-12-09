'use strict';

const new_game = document.getElementById('new_game');
const highscores = document.getElementById('highscores');
const name_input = document.getElementById('name_input');
const x = document.querySelector('span');
const name_submit = document.getElementById('name_submit');

new_game.addEventListener('click', function() {
  name_input.showModal();
});

highscores.addEventListener('click', function() {
  window.location.href = '../highscores/highscores.html';
});

name_submit.addEventListener('click', function() {
  const player_name = document.getElementById('player_name').value;
  //add so it grabs and assigns the given player as the value over to python
  let start = confirm(`Start a new game as ${player_name}?`);
  if (start === false) {
    name_input.close();
  } else {
    //Stores name in a sessionStorage item so it can be read in game.html
    sessionStorage.setItem('player_name', player_name)
    //Redirection to the game
    window.location.href = '../game/game.html';
  }
});

x.addEventListener('click', function() {
  name_input.close();
});