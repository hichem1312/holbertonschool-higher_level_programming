#!/usr/bin/node
const { argv } = require('process');

function addition (x, y) {
  return parseInt(x) + parseInt(y);
}

if (!argv[2] || isNaN(argv[2]) || !argv[3] || isNaN(argv[3])) {
  console.log('NaN');
} else {
  console.log(addition(argv[2], argv[3]));
}
