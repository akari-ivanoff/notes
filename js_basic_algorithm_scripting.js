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
Return the length of the longest word in the provided sentence.
Your response should be a number.
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
Return an array consisting of the largest number from each provided sub-array. For simplicity, the provided array will contain exactly 4 sub-arrays.
Remember, you can iterate through an array with a simple for loop, and access each member with array syntax arr[i].
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