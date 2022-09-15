#!/usr/bin/node
const ax = require('axios').default;
const dicti = {};
const p = require('process');
const x = p.argv[2]
ax.get(x)
  .then(function (response) {
    for (let i = 0; i < response.data.length; i++) {
      if (response.data[i].completed === true) {
        dicti[response.data[i].userId] = 0;
      }
    }
    for (let i = 0; i < response.data.length; i++) {
      if (response.data[i].completed === true) {
        dicti[response.data[i].userId] = dicti[response.data[i].userId] + 1;
      }
    }
    console.log(dicti);
  })
  .catch(function (error) {
    console.log(error);
  });