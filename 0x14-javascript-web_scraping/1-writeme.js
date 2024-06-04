#!/usr/bin/node
// writing a string to a file
const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filepath, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
