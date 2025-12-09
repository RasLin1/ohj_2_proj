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
  // MUOKATTU J: uusi tapa aloittaa peli Flaskin kautta (voi poistaa jos rikkoo pelin)
  const player_name = document.getElementById('player_name').value.trim();
  // const player_name = document.getElementById('player_name').value; //VANHA KOODI

  if (player_name.length < 1) {
    alert('Please enter a name.');
    return;
  }
  //localStorage.setItem('game_id', 1234)
  // MUOKATTU J: lisätty fetch-yhteys Flask-peliin ja tallennus localStorageen
  const start = confirm(`Start a new game as ${player_name}`);
  // let start = confirm(`Start a new game as ${player_name}?`); //VANHA KOODI
  if (!start){
    name_input.close();
    return;
  }
  // if (start === false) { name_input.close(); } else { //VANHA KOODI ALKU

  fetch(`http://127.0.0.1:3000/mh_game/startGame?name=${encodeURIComponent(player_name)}`)
      .then(r => r.json())
      .then(data => {

        console.log("Game started:", data);

        localStorage.setItem("player_id", data.player_id);

        window.location.href = '/web_pages/game/game.html';
      })
      .catch(err => {
        console.error(err)
      });

  // sessionStorage.setItem('player_name', player_name); //VANHA KOODI
  // window.location.href = '../game/game.html'; //VANHA KOODI
});

x.addEventListener('click', function() {
  name_input.close();
});