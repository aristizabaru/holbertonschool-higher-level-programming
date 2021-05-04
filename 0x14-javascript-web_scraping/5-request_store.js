#!/usr/bin/node
'use strict';
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  } // Print the error if one occurred
  if (response.statusCode === 200) {
    fs.writeFile(fileName, body, 'utf8', function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
