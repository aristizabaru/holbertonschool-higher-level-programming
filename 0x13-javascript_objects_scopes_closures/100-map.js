#!/usr/bin/node
'use strict';
const data = require('./100-data').list;

const newData = data.map(function (value, index) {
  return value * index;
});
console.log(data);
console.log(newData);
