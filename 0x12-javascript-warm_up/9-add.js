#!/usr/bin/node
const newArray = process.argv.slice(1);
function add(a, b) {
  let returnArray = a + b;
  console.log(returnArray);
}
add(Number(newArray[1]), Number(newArray[2]));
