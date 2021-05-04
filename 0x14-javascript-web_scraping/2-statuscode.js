#!/usr/bin/node
'use strict';
const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error(error);
    return;
  } // Print the error if one occurred
  console.log('code:', response.statusCode); // Print the response status code if a response was received
});
