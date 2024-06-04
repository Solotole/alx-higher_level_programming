#!/usr/bin/node
// writing a string to a file
const fs = require('fs');
const file_path = process.argv[2]
const content = process.argv[3]

fs.writeFile(file_path, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
