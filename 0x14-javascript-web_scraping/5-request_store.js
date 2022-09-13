#!/usr/bin/node
const f = require('fs');
const ax = require('axios').default;
const v = require('process');
const x = v.argv[2]
ax.get(x)
  .then(function (response) {
    f.writeFile(v.argv[3], response.data, (err) => {
      if (err) throw err;
    });
  });
