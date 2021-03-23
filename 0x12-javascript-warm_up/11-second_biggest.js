#!/usr/bin/node
'use strict';
let numbers = process.argv.slice(2);
let result = 0;

function getUnique (value, index, self) {
  return (self.indexOf(value) === index);
}

if (numbers.length > 1) {
  numbers = numbers.filter(getUnique);
  numbers.sort(function (a, b) { return b - a; });
  result = numbers[1];
}
console.log(result);
