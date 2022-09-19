#!/usr/bin/node
const x = require('fs');
const a = x.readFileSync(process.argv[2]);
const b = x.readFileSync(process.argv[3]);
x.writeFile(process.argv[4], a + b, function (err) {
  if (err) throw err;
});
