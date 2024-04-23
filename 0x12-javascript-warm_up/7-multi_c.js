#!/usr/bin/node
const newArray = process.argv.slice(1);
if (!Number(newArray[1])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(newArray[1]); i++) {
    console.log('C is fun');
  }
}
