#!/usr/bin/node
'use strict';
const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
