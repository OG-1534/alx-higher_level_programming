#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let x = 0; x < list.length; x++) {
    count = (list[x] === searchElement ? count + 1 : count);
  }

  return count;
};
