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
}
module.exports = Rectangle;
