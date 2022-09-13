#!/usr/bin/node
const ax = require('axios').default;
const v = require('process');
const x = v.argv[2];
ax.get('https://swapi-api.hbtn.io/api/films')
  .then(function (response) {
    console.log(response.data.results[x - 1].title);
  })
  .catch(function (error) {
    console.log(error);
  });
