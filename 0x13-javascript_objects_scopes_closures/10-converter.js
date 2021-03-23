#!/usr/bin/node
'use strict';
exports.converter = function (base) {
  function myConverter (num) {
    return num.toString(base);
  }
  return myConverter;
};
