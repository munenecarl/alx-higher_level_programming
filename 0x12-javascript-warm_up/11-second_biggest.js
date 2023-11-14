#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let biggestNum = Number(process.argv[2]);
  let secondBiggest = Number(process.argv[3]);

  if (biggestNum < secondBiggest) {
    [biggestNum, secondBiggest] = [secondBiggest, biggestNum];
  }

  for (let index = 4; index < process.argv.length; index++) {
    const currentNum = Number(process.argv[index]);
    if (currentNum > biggestNum) {
      secondBiggest = biggestNum;
      biggestNum = currentNum;
    } else if (currentNum > secondBiggest) {
      secondBiggest = currentNum;
    }
  }

  console.log(secondBiggest);
}
