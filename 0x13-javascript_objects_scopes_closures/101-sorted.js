#!/usr/bin/node
'use strict';
const data = require('./101-data').dict;
const newData = {};
for (const key in data) {
  if (newData[data[key]] === undefined) {
    newData[data[key]] = [];
  }
  newData[data[key]].push(key);
}
console.log(newData);
