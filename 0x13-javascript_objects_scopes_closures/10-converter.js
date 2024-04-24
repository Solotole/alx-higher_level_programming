#!/usr/bin/node
exports.converter = function (base) {
  return function (numberFirst) {
    return numberFirst.toString(base);
  };
};
