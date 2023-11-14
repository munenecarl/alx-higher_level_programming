#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let index = 0; index < Number(process.argv[2]); index++) {
    let row = '';
    for (let secondIndex = 0; secondIndex < Number(process.argv[2]); secondIndex++) {
      row += 'X';
    }
    console.log(row);
  }
}
