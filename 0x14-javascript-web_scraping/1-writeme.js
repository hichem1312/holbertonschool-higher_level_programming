#!/usr/bin/node
const fs = require('fs');
const v = require('process');
x = v.argv[2]
y = v.argv[3]
fs.writeFile(x, y, (err) => {
  if (err) throw err;
});
