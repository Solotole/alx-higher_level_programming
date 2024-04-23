#!/usr/bin/node
// constrictor method introduction
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

  rotate () {
    const newValue = this.width;
    this.width = this.height;
    this.height = newValue;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
