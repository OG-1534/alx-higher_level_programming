#!/usr/bin/node

/**
 * class Rectangle that defines a rectangle
 * constructor must take 2 arguments width(w) and height (h)
 * If w or h is equal to 0 or not a positive integer, create an empty object
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
