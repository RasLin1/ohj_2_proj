'use strict'

function startGame() {
  const name = prompt('Enter player name: ', 'tester');

  const myRequest = new Request(
      `/api/test_start?name=${encodeURIComponent(name)}`);

  fetch(myRequest)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        const output = document.getElementById('output').textContent =
            JSON.stringify(data, null, 2);
      })
      .catch((error) => {
        console.error('Error', error);
      })
}

