//===========================================================================
/*
Convert Celsius to Fahrenheit
The algorithm to convert from Celsius to Fahrenheit is the temperature in Celsius times 9/5, plus 32.
*/
function convertToF(celsius) {
  return (32 + celsius * 9 / 5);
}
convertToF(30);
//===========================================================================
/*
Reverse a String
Reverse the provided string. You may need to turn the string into an array before you can reverse it. Your result must be a string.
*/
function reverseString(str) {
  return str.split(``).reverse().join(``);
}
console.log(reverseString("hello"));
//===========================================================================
/*
Factorialize a Number
Return the factorial of the provided integer.
If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.
Factorials are often represented with the shorthand notation n!
For example: 5! = 1 * 2 * 3 * 4 * 5 = 120
Only integers greater than or equal to zero will be supplied to the function.
*/
function factorialize(num) {
  let factorial = 1;
  for (let i = 1; i <= num; i++) {
    factorial *= i;
  }
  return factorial;
}
console.log(factorialize(5));
//===========================================================================
/*
Find the Longest Word in a String
Return the length of the longest word in the provided sentence. Your response should be a number.
*/
function findLongestWordLength(str) {
  const arr = str.split(` `);
  arr.sort((a, b) => b.length - a.length);
  return arr[0].length;
}
findLongestWordLength("The quick brown fox jumped over the lazy dog");
//===========================================================================
/*
Return Largest Numbers in Arrays
Return an array consisting of the largest number from each provided sub-array. For simplicity, the provided array will contain exactly 4 sub-arrays. Remember, you can iterate through an array with a simple for loop, and access each member with array syntax arr[i].
*/
function largestOfFour(arr) {
  let resultArr = [];
  for (let i = 0; i < arr.length; i++) {
    arr[i].sort((a, b) => b - a);
    resultArr.push(arr[i][0]);
  }
  return resultArr;
}
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
//===========================================================================
/*
Confirm the Ending
Check if a string (first argument, str) ends with the given target string (second argument, target).
This challenge can be solved with the .endsWith() method, which was introduced in ES2015. But for the purpose of this challenge, we would like you to use one of the JavaScript substring methods instead.
*/
function confirmEnding(str, target) {
  // "Never give up and good luck will find you."
  // -- Falcor
  const strArr = str.split(``).reverse();
  const targetArr = target.split(``).reverse();
  let i = 0;
  while(i < targetArr.length) {
    if (targetArr[i] !== strArr[i]) {
      return false
    }
    i++;
  }
  return true;
}
confirmEnding("Bastian", "n");
//===========================================================================
/*
Repeat a String Repeat a String
Repeat a given string str (first argument) for num times (second argument). Return an empty string if num is not a positive number. The built-in repeat()-method should not be used.
*/
function repeatStringNumTimes(str, num) {
  // repeat after me
  if (num <= 0) {
    return ``;
  } else {
    let resultStr = ``;
    for (let i = 1; i <= num; i++) {
      resultStr += str;
    }
  return resultStr;
  }
}
console.log(repeatStringNumTimes("abc", 3));
//===========================================================================
/*
Truncate a String
Truncate a string (first argument) if it is longer than the given maximum string length (second argument). Return the truncated string with a ... ending.
*/
function truncateString(str, num) {
  // Clear out that junk in your trunk
  if (str.length <= num) {
    return str;
  } else {
    const strArr = str.split(``);
    const resultArr = [];
    for (let i = 0; i < num; i++) {
      resultArr.push(strArr[i]);
    }
    return resultArr.join(``) + `...`;
  } 
}
truncateString("A-tisket a-tasket A green and yellow basket", 8);
//===========================================================================
/*
Finders Keepers
Create a function that looks through an array (first argument) and returns the first element in the array that passes a truth test (second argument). If no element passes the test, return undefined.
*/
function findElement(arr, func) {
  let i = 0;
  while (i < arr.length) {
    if (func(arr[i]) === true) {
      return arr[i];
    }
    i++;
  }
  return undefined;
}
findElement([1, 2, 3, 4], num => num % 2 === 0);
//===========================================================================
/*
Boo who
Check if a value is classified as a boolean primitive. Return true or false. Boolean primitives are true and false.
*/
function booWho(bool) {
  // What is the new fad diet for ghost developers? The Boolean.
  return bool === true || bool === false;
}
booWho(null);
//===========================================================================
/*
Title Case a Sentence
Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case. For the purpose of this exercise, you should also capitalize connecting words like "the" and "of".
*/
function titleCase(str) {
  return str.split(` `).map( (item) => 
    item.charAt(0).toUpperCase() + item.slice(1).toLowerCase()
  ).join(` `);
}
titleCase("I'm a little tea pot");
//===========================================================================
/*
Slice and Splice
You are given two arrays and an index. Use the array methods slice and splice to copy each element of the first array into the second array, in order. Begin inserting elements at index n of the second array. Return the resulting array. The input arrays should remain the same after the function runs.
*/
function frankenSplice(arr1, arr2, n) {
  // It's alive. It's alive!
  const arr = [...arr2];
  arr.splice(n, 0, ...arr1);
  return arr;
  // Another solution:
  // return arr2.slice(0, n).concat(arr1.concat(arr2.slice(n, arr2.length)));
}
frankenSplice([1, 2, 3], [4, 5, 6], 1);
//===========================================================================
/*
Falsy Bouncer
Remove all falsy values from an array. Falsy values in JavaScript are false, null, 0, "", undefined, and NaN. Hint: Try converting each value to a Boolean.
*/
function bouncer(arr) {
  // Don't show a false ID to this bouncer.
  const resultArr = [];
  for (let i = 0; i < arr.length; i++) {
    if (Boolean(arr[i]) == true) {
      resultArr.push(arr[i]);
    }
  }
  return resultArr;
}
bouncer([7, "ate", "", false, 9]);
//===========================================================================
/*
Where do I Belong
Return the lowest index at which a value (second argument) should be inserted into an array (first argument) once it has been sorted. The returned value should be a number.
For example, getIndexToIns([1,2,3,4], 1.5) should return 1 because it is greater than 1 (index 0), but less than 2 (index 1).
Likewise, getIndexToIns([20,3,5], 19) should return 2 because once the array has been sorted it will look like [3,5,20] and 19 is less than 20 (index 2) and greater than 5 (index 1).
*/
function getIndexToIns(arr, num) {
  // Find my place in this sorted array.
  arr.sort((a, b) => a - b);
  if (arr.length === 0 || num <= arr[0]) {
    return 0;
  } else if (num > arr[arr.length - 1]) {
    return arr.length;
  } else {
    for (let i = 0; i <= arr.length - 2; i++) {
      if ((num > arr[i]) && (num <= arr[i + 1])) {
        return i + 1;
      }
    }
  }
}
getIndexToIns([40, 60], 50);
//===========================================================================
/*
Mutations
Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array.
For example, ["hello", "Hello"], should return true because all of the letters in the second string are present in the first, ignoring case.
The arguments ["hello", "hey"] should return false because the string "hello" does not contain a "y".
Lastly, ["Alien", "line"], should return true because all of the letters in "line" are present in "Alien".
*/
function mutation(arr) {
  let firstArr = arr[0].toLowerCase().split(``);
  let secondArr = arr[1].toLowerCase().split(``);
  for (let i = 0; i < secondArr.length; i++) {
    let idx = firstArr.indexOf(secondArr[i]);
    if (idx === -1) {
      return false
    }
    // else {
      // firstArr.splice(idx, 1);
    // }
  }
  return true;
}
mutation(["hello", "hey"]);
//===========================================================================
/*
Chunky Monkey
Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a two-dimensional array.
*/
function chunkArrayInGroups(arr, size) {
  // Break it up.
  const resultArr = [];
  for (let i = 0; i < arr.length; i += size) {
    resultArr.push(arr.slice(i, i + size));
    console.log(resultArr);
  }
  return resultArr;
}
console.dir(chunkArrayInGroups(["a", "b", "c", "d"], 2));
//===========================================================================