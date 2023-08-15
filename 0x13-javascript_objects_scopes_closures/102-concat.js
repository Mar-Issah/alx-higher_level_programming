#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];

try {
  const content1 = fs.readFileSync(fileA, 'utf-8');
  const content2 = fs.readFileSync(fileB, 'utf-8');

  const concatContent = content1 + content2;

  fs.writeFileSync(destinationFile, concatContent);

  console.log(concatContent);
} catch (error) {
  console.error('An error occurred:', error.message);
}
