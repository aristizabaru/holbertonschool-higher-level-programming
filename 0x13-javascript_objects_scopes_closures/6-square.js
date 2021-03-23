#!/usr/bin/node
'use strict';
const SquareDuplicate = require('./5-square.js');
module.exports = class Square extends SquareDuplicate {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
