#!/usr/bin/node
// print method introduction
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rowXs = '';
      for (let j = 0; j < this.width; j++) {
        rowXs += 'X';
      }
      console.log(rowXs);
    }
  }
}
module.exports = Rectangle;
