#!/usr/bin/node
// reading and printing contents of a file
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
