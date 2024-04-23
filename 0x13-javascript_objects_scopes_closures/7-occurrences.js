#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let countOccurences = 0;
  const lengthList = list.length;
  for (let i = 0; i < lengthList; i++) {
    if (list[i] === searchElement) {
      countOccurences += 1;
    } else {
      continue;
    }
  }
  return countOccurences;
};
