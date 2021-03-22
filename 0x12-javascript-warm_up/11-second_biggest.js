#!/usr/bin/node
'use strict';
const numbers = process.argv.sort();
if (numbers.length <= 3) {
  console.log(0);
} else {
  console.log(numbers[numbers.length - 2]);
}
