#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const object = JSON.parse(body);
    for (let j = 0; j < object.results.length; j++) {
      for (let i = 0; i < object.results[j].characters.length; i++) {
        if (object.results[j].characters[i] === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count = count + 1;
        } else {
          continue;
        }
      }
    }
  }
  console.log(count);
});
