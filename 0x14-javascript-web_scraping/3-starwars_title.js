#!/usr/bin/node
'use strict';
const request = require('request');
const id = process.argv[2];

request('https://swapi-api.hbtn.io/api/films/' + id, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  } // Print the error if one occurred
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
