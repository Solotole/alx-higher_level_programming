#!/usr/bin/node
const originalList = require('./101-data.js').dict;
const userOccurences = {};

for (const userId in dict) {
  const occur = dicy[userId];
  if (!userOccurences[occur]) {
    userOccurences[occur] = [];
  }
  userOccurences[occur].push(userId);
}

console.log(userOccurences);
