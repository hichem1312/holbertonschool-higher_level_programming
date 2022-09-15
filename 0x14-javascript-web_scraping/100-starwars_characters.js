#!/usr/bin/node
const ax = require('axios').default;
const p = require('process');
const x = p.argv[2];
ax.get('https://swapi-api.hbtn.io/api/films/')
  .then(function (response) {
    for (let i = 0; i < response.data.results[x - 1].characters.length; i++) {
      axios.get(response.data.results[x - 1].characters[i])
        .then(function (response2) {
          console.log(response2.data.name);
        });
    }
  }
  );