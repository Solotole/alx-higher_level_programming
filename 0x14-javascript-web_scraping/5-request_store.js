#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const filepath = process.argv[3];
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // const data = JSON.stringify(body);
    fs.writeFile(filepath, body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
