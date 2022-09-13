#!/usr/bin/node
const fs = require('fs');
const argem = process.argv.slice(2);
fs.readFile(argem[0], (err, buff) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(buff.toString());
});
