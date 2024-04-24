#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let varDeterminant = 0;
  while (varDeterminant < x) {
    theFunction();
    varDeterminant += 1;
  }
};
