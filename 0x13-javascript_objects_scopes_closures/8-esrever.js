#!/usr/bin/node
exports.esrever = function (list) {
  const listLength = list.length - 1;
  let newListIndex = 0;
  let newList = [];
  for (let i = listLength; i >= 0; i--) {
    newList[newListIndex] = list[i];
    newListIndex += 1;
  }
  return newList;
};
