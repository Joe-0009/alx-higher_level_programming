#!/bin/usr/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  cosole.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('C is fun');
}
