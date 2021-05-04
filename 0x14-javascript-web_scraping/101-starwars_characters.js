#!/usr/bin/node
'use strict';

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const cast = [];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  } // Print the error if one occurred
  if (response.statusCode === 200) {
    const jsonData = JSON.parse(body);
    const castURL = jsonData.characters;
    fetchCast(castURL, castURL.length - 1);
  }
});

function fetchCast (castURL, idx) {
  // base case
  if (idx === -1) {
    for (let i = cast.length - 1; i > -1; i--) {
      console.log(cast[i]);
    }
    return;
  }
  const url = castURL[idx];
  request(url, function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    } // Print the error if one occurred
    if (response.statusCode === 200) {
      cast.push(JSON.parse(body).name);
      fetchCast(castURL, idx - 1);
    }
  });
}
