#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
const line1 = fs.readFileSync(fileA, 'utf8');
const line2 = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, line1 + line2, 'utf8');
