#!/bin/usr/node
if (isNaN(process.argv[2])) {
  cosole.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
}
