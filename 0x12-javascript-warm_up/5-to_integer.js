#!/usr/bin/node
const newArray = process.argv.slice(1);
if (!Number(newArray[1])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + newArray[1]);
}
