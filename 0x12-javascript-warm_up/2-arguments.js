#!/usr/bin/node
const sizeArray = process.argv.slice(1);
if (sizeArray.length === 1) {
  console.log('No argument');
} else if (sizeArray.length === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
