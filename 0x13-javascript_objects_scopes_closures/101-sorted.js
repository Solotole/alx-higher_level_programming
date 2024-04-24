#!/usr/bin/node
const originalDict = require('./101-data.js').dict;
const userOccurences = {};

for (const userId in originalDict) {
  const occurEnces = originalDict[userId];
  if (!userOccurences[occurEnces]) {
    userOccurences[occurEnces] = [];
  }
  userOccurences[occurEnces].push(userId);
}

console.log(userOccurences);
