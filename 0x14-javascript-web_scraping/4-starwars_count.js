#!/usr/bin/node
'use strict';
const request = require('request');
const endPoint = process.argv[2];
const characterID = '18';

request(endPoint, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  } // Print the error if one occurred
  if (response.statusCode === 200) {
    const jsonData = JSON.parse(body);
    console.log(findCharacter(jsonData));
  }
});

function findCharacter (jsonData) {
  let characterCount = 0;

  for (const movie of jsonData.results) {
    for (const character of movie.characters) {
      if (character.endsWith(characterID + '/')) {
        characterCount += 1;
      }
    }
  }
  return characterCount;
}
