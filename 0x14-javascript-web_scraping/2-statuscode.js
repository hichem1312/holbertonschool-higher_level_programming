#!/usr/bin/node
const r = require('request');
const x = process.argv[2];
r.get(x).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
