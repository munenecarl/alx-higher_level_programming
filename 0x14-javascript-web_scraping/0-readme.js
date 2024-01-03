#!/usr/bin/node
// Reads content in a file
const fs = require('fs');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
