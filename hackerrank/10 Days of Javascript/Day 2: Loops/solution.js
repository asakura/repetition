'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}


function isVowel(c) {
  switch (c) {
    case 'a':
      return true;

    case 'e':
      return true;

    case 'i':
      return true;

    case 'o':
      return true;

    case 'u':
      return true;

    default:
      return false;
  }
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
  for (let i = 0; i < s.length; i++) {
    if (isVowel(s[i])) {
      console.log(s[i]);
    }
  }

  for (let i = 0; i < s.length; i++) {
    if (!isVowel(s[i])) {
      console.log(s[i]);
    }
  }
}


function main() {
    const s = readLine();

    vowelsAndConsonants(s);
}
