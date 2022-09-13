#!/usr/bin/node
const ax = require('axios').default;
const v = require('process');
const x = (v.argv[2])
let z = 0;
ax.get(x)
  .then(function (response) {
    for (let a = 0; a < response.data.results.length; a++) {
      for (let b = 0; b < response.data.results[a].characters.length; b++) {
        if (response.data.results[a].characters[b] === 'https://swapi-api.hbtn.io/api/people/18/') { z++; }
      }
    }
    console.log(z);
  });
