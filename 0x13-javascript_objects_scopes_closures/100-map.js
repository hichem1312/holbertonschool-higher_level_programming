#!/usr/bin/node
array = require('./100-data.js').list;
const i = 0;
console.log(array);
const x = array.map(a => a * i++);
console.log(x);