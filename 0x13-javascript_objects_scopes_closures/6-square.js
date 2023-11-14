#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c == null) {
      this.print();
    } else {
      for (let index = 0; index < this.height; index++) {
        let row = '';
        for (let secondIndex = 0; secondIndex < this.width; secondIndex++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
};
