#!/usr/bin/node
const newArray = process.argv.slice(1);
let returnValue;
// the factorial variable declared
function factorial(value) {
  if (!Number(value)) {
    return 1;
  }
  if (Number(value) === 0 || Number(value) === 1) {
    return 1;
  }
  return value * factorial(value - 1);
}
returnValue = factorial(newArray[1]);
console.log(returnValue);
