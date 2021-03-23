#!/usr/bin/node
'use strict';
exports.nbOccurences = function (list, searchElement) {
  let sum = 0;
  list.forEach(element => {
    if (element === searchElement) {
      sum++;
    }
  });
  return (sum);
};
