#!/usr/bin/node
const ax = require('axios').default;
const v = require('process');
const x = v.argv[2]
ax.get(x)
  .then(function (response) {
    console.log('code:', response.status);
  })
  .catch(function (error) {
    console.log('code:', error.response.status);
  });
