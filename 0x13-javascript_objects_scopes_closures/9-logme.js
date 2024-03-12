#!/usr/bin/node

let theCounter = 0;

exports.logMe = function count (item) {
  console.log(`${theCounter}: ${item}`);
  theCounter += 1;
};
