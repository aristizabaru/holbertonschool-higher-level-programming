#!/usr/bin/node
let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];
let fs = require('fs');
let line1 = fs.readFileSync(fileA, 'utf8')
let line2 = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, line1 + line2, 'utf8');
