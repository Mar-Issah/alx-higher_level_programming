#!/usr/bin/node
const args = process.argv.slice(2);
const sortedArgs = uniqueArgs.sort((a, b) => b - a);

console.log(sortedArgs.length <= 1 ? sortedArgs[1] : console.log(0));
