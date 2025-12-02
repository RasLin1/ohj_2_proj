'use strict'

const new_game = document.getElementById('new_game')
const highscores = document.getElementById('highscores')
const name_input = document.getElementById('name_input')

new_game.addEventListener('click', function(){
  name_input.showModal()
})