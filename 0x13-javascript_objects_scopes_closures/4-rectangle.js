#!/usr/bin/node
/**
 * class Rectangle that defines a rectangle
 * constructor must take 2 arguments: w and h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * instance method print() prints the rectangle using the character X
 * instance method rotate() exchanges the w and the h of the rectangle
 * instance method double() multiples the w and the h of the rectangle by 2
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let j = 0;
      while (j < this.width) {
        myVar += 'X';
        j++;
      }

      console.log(myVar);
    }
  }
	rotate () {
		let temp = 0;
		temp = this.width;
		this.width = this.height;
		this.height = temp;
	}

	double () {
		this.width *= 2;
		this.height *= 2;
	}
}
module.exports = Rectangle;
