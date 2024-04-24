#!/usr/bin/node
const newArray = process.argv.slice(1);
if (!Number(newArray[1])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(newArray[1]); i++) {
    let printXs = '';
    for (let j = 0; j < Number(newArray[1]); j++) {
      printXs += 'X';
    }
    console.log(printXs);
  }
}
