#!/usr/bin/node

function recursiveFunction (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  }
  return num * recursiveFunction(num - 1);
}

console.log(recursiveFunction(parseInt(process.argv[2])));
