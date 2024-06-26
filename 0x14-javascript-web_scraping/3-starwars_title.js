#!/usr/bin/node
// requesting and displaying title from json object
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const javaobject = JSON.parse(body);
    console.log(javaobject.title);
  }
});
