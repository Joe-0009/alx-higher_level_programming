#!/usr/bin/node;

// Extract command-line arguments starting from index 2 and convert them to integers
const numbers = process.argv.slice(2).map(Number);

// Sort the numbers in descending order
numbers.sort((a, b) => b - a);

if (numbers.length <= 1) {
    console.log(0);
} else {
    console.log(numbers[1]);
}
