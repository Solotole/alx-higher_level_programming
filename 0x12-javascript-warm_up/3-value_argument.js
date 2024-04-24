#!/usr/bin/node
const newArray = process.argv.slice(1);
if (!newArray[1]) {
  console.log('No argument');
} else {
  console.log(newArray[1]);
}
