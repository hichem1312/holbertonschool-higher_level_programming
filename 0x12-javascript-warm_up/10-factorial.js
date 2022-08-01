#!/usr/bin/node
const { argv } = require('process');

function fact (x) {
  if (x === 1) {
    return x;
  }
  return x * fact(x - 1);
}

if (!argv[2] || isNaN(argv[2])) {
  console.log(1);
} else {
  const a = parseInt(argv[2]);
  console.log(fact(a));
}
