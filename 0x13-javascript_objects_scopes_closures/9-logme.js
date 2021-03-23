#!/usr/bin/node
'use strict';
let i = 0;
exports.logMe = function (item) {
  console.log(`${i}: ${item}`);
  i++;
};
