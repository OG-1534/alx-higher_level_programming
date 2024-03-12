#!/usr/bin/node

/**
 * class Square that defines a square
 * and inherits from Square of 5-square.js
 * instance method charPrint(c) prints the rectangle using the char c
 * If c is undefined, use the character X
 */

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let j = 0;
      while (j < this.width) {
        myVar += myChar;
        j++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
