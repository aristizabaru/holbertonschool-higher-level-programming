#!/usr/bin/node
'use strict';

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

request(url + id, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  } // Print the error if one occurred
  if (response.statusCode === 200) {
    const jsonData = JSON.parse(body);
    fetchCast(jsonData);
  }
});

function fetchCast(jsonData) {
  const cast = [];
  for (const actorURL of jsonData.characters) {
    request(actorURL, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      } // Print the error if one occurred
      if (response.statusCode === 200) {
        console.log(JSON.parse(body).name);
      }
    });
  }
}