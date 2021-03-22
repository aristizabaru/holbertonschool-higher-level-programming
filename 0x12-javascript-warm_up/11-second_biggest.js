#!/usr/bin/node
'use strict';
const numbers = process.argv.slice(2);
let result = 0;
if (numbers.length > 1) {
  numbers.sort();
  result = numbers[numbers.length - 2];
}
console.log(result);
