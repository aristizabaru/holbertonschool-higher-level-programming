#!/usr/bin/node
'use strict';
const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];

fs.writeFile(path, content, 'utf8', function (err) {
  if (err) {
    console.error(err);
  }
});
