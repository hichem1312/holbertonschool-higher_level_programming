#!/usr/bin/node
const fs = require('fs');
const process = require('process');
x = process.argv[2]
y = process.argv[3]
fs.writeFile(x, y, (err) => {
  if (err) throw err;
});
