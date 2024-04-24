#!/usr/bin/node
const oldList = require('./100-data.js').list;
const newerArray = oldList.map((value, index) => value * index);
console.log(oldList);
console.log(newerArray);
