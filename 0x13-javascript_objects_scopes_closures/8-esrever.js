#!/usr/bin/node
exports.esrever = function (list) {
  let listLength = list.length - 1;
  let newListIndex = 0;
  let newList = [];
  while (listLength >= 0) {
    newList[newListIndex] = list[listLength];
    newListIndex += 1;
    listLength -= 1;
  }
  return newList;
}
