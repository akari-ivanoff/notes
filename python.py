"""
Download Python 3.4
https://www.python.org/downloads/release/python-343/

The Python Standard Library
https://docs.python.org/3/library/index.html

The Python Visualizer
http://pythontutor.com/visualize.html#mode=edit

Python tutorial and reference
https://www.w3schools.com/python/default.asp

# ==============================================================================================
#Arithmetic Operators
Operator	Operation			Expression	English description	Result
+			addition			11 + 56		11 plus 56			67
-			subtraction			23 - 52		23 minus 52			-29
*			multiplication		4 * 5		4 multiplied by 5	20
**			exponentiation		2 ** 5		2 to the power of 5	32
/			division			9 / 2		9 divided by 2		4.5
//			integer division	9 // 2		9 divided by 2		4
%			modulo (remainder)	9 % 2		9 mod 2				1

# ==============================================================================================
#Arithmetic Operator Precedence
When multiple operators are combined in a single expression, the operations are evaluated in order of precedence.

Operator						Precedence
**								highest
- (negation)					.
*, /, //, %						.
+ (addition), - (subtraction)	lowest

# ==============================================================================================
#Types

int: integer
For example: 3, 4, 894, 0, -3, -18

float: floating point number (an approximation to a real number)
For example: 5.6, 7.342, 53452.0, 0.0, -89.34, -9.5

str: A string literal is a sequence of characters. In Python, this type is called str. Strings in Python start and end with a single quotes (') or double quotes ("). The third string format uses triple-quotes and a triple-quoted string can span multiple lines. A string can be made up of letters, numbers, and special characters.

bool: The Python type bool has two values: True and False. There are also three logical operators that produce Boolean values: and, or, and not.

# ==============================================================================================
#Strings in Python

Escape Sequences
To include a quote within a string, use an escape character (\) before it. The escape sequence \' indicates that the second quote is simply a quote, not the end of the string. An alternative approach is to use a double-quoted string when including a single-quote within it, or vice-versa. Single- and double-quoted strings are equivalent.
Escape Sequence		Name
\n					newline (ASCII linefeed - LF) 
\t					tab (ASCII horizontal tab - TAB)
\\					backslash (\)
\'					single quote (')
\"					double quote (")

String Operators
Expression		Description							Example				Output
str1 + str2		concatenate str1 and str1			print('ab' + 'c')	abc
str1 * int1		concatenate int1 copies of str1		print('a' * 5)		aaaaa
int1 * str1		concatenate int1 copies of str1		print(4 * 'bc')		bcbcbcbc

The * and + operands obey by the standard precedence rules when used with strings.
All other mathematical operators and operands result in a TypeError.

String Comparisons
The equality and inequlity operators can be applied to strings. We can compare two strings for their dictionary order, comparing them letter by letter. Capitalization matters, and capital letters are less than lowercase letters.

Testing For Substrings
The operator in checks whether a string appears anywhere inside another one (that is, whether a string is a substring of another).

>>> 'c' in 'aeiou'
False
>>> 'cad' in 'abracadabra'
True

String length: function len
The builtin function len returns the number of characters in a string:

>>> len('')
0
>>> len('abracadabra')
11
>>> len('Bwa' + 'ha' * 10)
23

Description				Operator	Example					Result of example
inequality				!=			'cat' != 'Cat'				True
equality				==			'cat' == 'cat'				True
less than				<			'A' < 'a'					True
greater than			>			'a' > 'A'					True
less than or equal		<=			'a' <= 'a'					True
greater than or equal	>=			'a' >= 'A'					True
contains				in			'cad' in 'abracadabra'		True
length of str s			len(s)		len("abc")					3

Indexing
An index is a position within the string. Positive indices count from the left-hand side with the first character at index 0, the second at index 1, and so on. Negative indices count from the right-hand side with the last character at index -1, the second last at index -2, and so on.
Let s refer to 'Learn to Program'.
The first character of the string is at index 0 and can be accessed using this bracket notation:

>>> s[0]
'L'
>>> s[1]
'e'
Negative indices are used to count from the end (from the right-hand side):
>>> s[-1]
'm'

Slicing
We can extract more than one character using slicing. A slice is a substring from the start index up to but not including the end index. For example:

>>> s[0:5]
'Learn'

More generally, the end of the string can be represented using its length:
>>> s[9:len(s)]
'Program'

The end index may be omitted entirely and the default is len(s):
>>> s[9:]
'Program'

Similarly, if the start index is omitted, the slice starts from index 0:
>>> s[:]
'Learn to Program'

Negative indices can be used for slicing too. The following three expressions are equivalent:
>>> s[1:8]
'earn to'

The slicing and indexing operations do not modify the string that they act on, so the string that s refers to is unchanged by the operations above. In fact, we cannot change a string. Operations like the following result in errors:

>>> s[6] = 'd'

The slicing and indexing operations do not modify the string that they act on, so the string that s refers to is unchanged by the operations above. In fact, we cannot change a string. Operations like the following result in errors:

>>> s[6] = 'd'
Traceback (most recent call last):
        File <"pyshell#19", line 1, in <module>
                s[6] = 'd'
TypeError: 'str' object does not support item assignment

Imagine that we want to change string s to refer to 'Learned to Program'. The following expression evaluates to that 'Learned to Program': s[:5] + 'ed' + s[5:]

Variable s gets the new string: s = s[:5] + 'ed' + s[5:]

Notice that the string that s originally referred to was not modified: strings cannot be modified. Instead a new string was created and s was changed to point to that string.


# ==============================================================================================
Boolean values

Comparison operators
The comparison operators take two values and produce a Boolean value.

Description					Operator
less than					<
greater than				>
equal to					==
greater than or equal to	>=
less than or equal to		<=
not equal to				!=


# ==============================================================================================
#Variable names
The rules for legal Python names:
	1. Names must start with a letter or _.
	2. Names must contain only letters, digits, and _.
For Python, in most situations, the convention is to use pothole_case.

# ==============================================================================================
#Built-in Functions

Function dir
Python has a set of built-in functions. To see the list of built-in functions, run dir(__builtins__):

Function help
To get information about a particular function, call help and pass the function as the argument. For example: help(abs)

Function print
Python has a built-in function named print that displays messages to the user. 
>>> print("hello")
hello
>>> print(3 + 7 - 3)
7
>>> print("hello", "there")
hello there

Function input
The function input is a built-in function that prompts the user to enter some input. The program waits for the user to enter the input, before executing the subsequent instructions. The value returned from this function is always a string. 
>>> input("What is your name? ")
What is your name? Jen
'Jen'
>>> num_coffee = input("How many cups of coffee? ")
How many cups of coffee? 2
>>> num_coffee
'2'

Function str
Builtin function str takes any value and returns a string representation of that value.
>>> str(3)
'3'

Function int
Builtin function int takes a string containing only digits (possibly with a leading minus sign -) and returns the int that represents. Function int also converts float values to integers by throwing away the fractional part.
>>> int('12345')
12345

Function float
Builtin function float takes a string containing only digits and zero or one decimal points (possibly with a leading minus sign -) and returns the float that represents. Function float also converts int values to floats.
>>> float('-43.2')
-43.2

Function: range
Python has a built-in function called range that is useful to use when you want to generate a sequence of numbers. You can type help(range) in IDLE if you ever need a reminder.

The example below will print the integers 0 to 9, inclusive.
for i in range(10):
    print (i)

The form of range is:
range([start,] stop[, step]):
    return a virtual sequence of numbers from start to stop by step

# ==============================================================================================
#Function Design Recipe - The Six Steps
1. Examples
	What should your function do?
	Type a couple of example calls.
	Pick a name (often a verb or verb phrase): What is a short answer to "What does your function do"?
2. Type Contract
	What are the parameter types?
	What type of value is returned?
3. Header
	Pick meaningful parameter names.
4. Description
	Mention every parameter in your description.
	Describe the return value.
5. Body
	Write the body of your function.
6. Test
	Run the examples.

# ==============================================================================================
Import: Using Non-Builtin Functions
Modules
Python contains many functions, but not all of them are immediately available as builtin functions. Instead of being available as builtins, some functions are saved in different modules. A module is a file containing function definitions and other statements.

We may also define our own modules with our own functions.

import
In order to gain access to the functions in a module, we must import that module.

The general form of an import statement is:
import module_name

To access a function within a module, we use:
module_name.function_name


# ==============================================================================================
The if statement
If statements can be used to control which instructions are executed. Here is the general form:

if expression1:    
    body1
[elif expression2:      0 or more clauses
    body2]
[else:                  0 or 1 clause
    bodyN]
elif stands for "else if", so this forms a chain of conditions.

To execute an if statement, evaluate each expression in order from top to bottom. If an expression produces True, execute the body of that clause and then skip the rest open the if statement. If there is an else, and none of the expressions produce True, then execute the body of the else. When execution of a function body ends without having executed a return statement, the function returns value None. The type of None is NoneType.

# ==============================================================================================
Methods
A method is a function inside of an object

The general form of a method call is:
object.method(arguments)

To find out which methods are inside strings, use the function dir:
>>> dir(str)

To get information about a method, such as the lower method, do the following:
>>> help(str.lower)

# ==============================================================================================
For Loops
The general form of a for loop over a string is:

for variable in str:
    body

The variable refers to each character of the string in turn and executes the body of the loop for each character. For example:

>>> s = 'yesterday'
>>> for char in s:
...     print(char)
... 
y
e
s
t
e
r
d
a
y    

Accumulator pattern: numeric accumulator
Consider the code below, in which the variable num_vowels is an accumulator:

def count_vowels(s):
    ''' (str) -> int

    Return the number of vowels in s. Do not treat letter y as a vowel
    
    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0    
    '''

    num_vowels = 0
    
    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    return num_vowels
The loop in the function above will loop over each character that s refers to, in turn. The body of the loop is executed for each character, and when a character is a vowel, the if condition is True and the value that num_vowels refers to is increased by one.

The variable num_vowels is an accumulator, because it accumulates information. It starts out referring to the value 0 and by the end of the function it refers to the number of vowels in s.

Accumulator pattern: string accumulator
In the following function, the variable vowels is also an accumulator:

def collect_vowels(s):
    ''' (str) -> str

    Return the vowels from s.  Do not treat the letter
    y as a vowel.

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    '''

    vowels = ''

    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels

Variable vowels initially refers to the empty string, but over the course of the function it accumulates the vowels from s.

# ==============================================================================================
IDLE's Debugger

1. Make sure the Python Shell window is on top and select Debug->Debugger. This opens a window called "Debug Control".
2. Check the checkbox for Source.
3. Open the Python file where you have saved your program.
4. Select Run->Run Module. This will change the contents of Debug Control.

# ==============================================================================================
while loops
The general form of a while loop:

while expression:
    statements
The while condition, num < 100, is evaluated, and if it is True the statements in the loop body are executed. The loop condition is rechecked and if found to be True, the body executes again. This continues until the loop condition is checked and is False. For example:

>>> num = 2
>>> while num < 100:
        num = num * 2
        print(num)


4
8
16
32
64
128
In the example above, there are 6 iterations: the loop body executes 6 times.
Loops Conditions and Lazy Evaluation
The problem: print the characters of str s, up to the first vowel in s.

The first attempt at solving this problem works nicely when s contains one or more vowel, but results in an error if there are no vowels in s:

>>> i = 0
>>> s = 'xyz'
>>> while not (s[i] in 'aeiouAEIOU'):
        print(s[i])
        i = i + 1


x
y
z
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    while not (s[i] in 'aeiouAEIOU'):
IndexError: string index out of range

In the code above, the error occurs when s is indexed at i and i is outside of the range of valid indices. To prevent this error, add an additional condition is added to ensure that i is within the range of valid indices for s:

>>> i = 0
>>> s = 'xyz'
>>> while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        print(s[i])
        i = i + 1


x
y
z
Because Python evaluates the and using lazy evaluation, if the first operand is False, then the expression evaluates to False and the second operand is not even evaluated. That prevents the IndexError from occurring.


# ==============================================================================================
Type list

Our programs will often work with collections of data. One way to store these collections of data is using Python's type list.

The general form of a list is:

[expr1, expr2, ..., exprN]
For example, here is a list of three grades:
grades = [80, 90, 70]

List Operations

Like strings, lists can be indexed:
>>> grades[0]
80

Lists can also be sliced, using the same notation as for strings:
>>> grades[0:2]
[80, 90]

The in operator can also be applied to check whether a value is an item in a list.
>>> 90 in grades
True

Several of Python's built-in functions can be applied to lists, including:

len(list): return the length of list.
min(list): return the smallest element in list.
max(list): return the largest element in list.
sum(list): return the sum of elements of list (where list items must be numeric).

Types of list elements
Lists elements may be of any type and contain elements of more than one type. For example, a street address can be represented by a list of [int, str]:

street_address = [10, 'Main Street']

for loops over list
Similar to looping over the characters of a string, it is possible to iterate over the elements of a list. For example:
>>> for grade in grades:
    print(grade)
80
90
70
                        
The general form of a for loop over a list is:
for variable in list:
    body

list.append(object) - Append object to the end of list:
>>> colours = ['yellow', 'blue']
>>> colours.append('red')
>>> print(colours)
['yellow', 'blue', 'red']

list.extend(list) - Append the items in the list parameter to the list:
>>> colours.extend(['pink', 'green'])
>>> print(colours)
['yellow', 'blue', 'red', 'pink', 'green']

list.pop([index]) - Remove the item at the end of the list; optional index to remove from anywhere:
>>> colours.pop()
'green'
>>> print(colours)
['yellow', 'blue', 'red', 'pink']
>>> colours.pop(2)
'red'
>>> print(colours)
['yellow', 'blue', 'pink']

list.remove(object) - Remove the first occurrence of the object; error if not there:
>>> colours.remove('green')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    colours.remove('green')
ValueError: list.remove(x): x not in list
>>> colours.remove('pink')
>>> print(colours)
['yellow', 'blue']    

list.reverse() - Reverse the list:
>>> grades = [95, 65, 75, 85]
>>> grades.reverse()
>>> print(grades)
[85, 75, 65, 95]

list.sort() - Sort the list from smallest to largest:	
>>> grades.sort()
>>> print(grades)
[65, 75, 85, 95]

list.insert(int, object) - Insert object at the given index, moving items to make room:
>>> grades.insert(2, 80)
>>> print(grades)
[65, 75, 80, 85, 95]

list.count(object) - Return the number of times object occurs in list:
>>> letters = ['a', 'a', 'b', 'c']
>>> letters.count('a')
2

list.index(object) - Return the index of the first occurrence of object; error if not there:
>>> letters.index('a')
0
>>> letters.index('d')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    letters.index('d')
ValueError: 'd' is not in list          

Parallel Lists and Strings
Two lists are parallel if they have the same length and the items at each index are somehow related. The items at the same index are said to be at corresponding positions.

Mutability
We say that lists are mutable: they can be modified. All the other types we have seen so far (str, int, float and bool) are immutable: they cannot be modified.

Lists can contain items of any type, including other lists. These are called nested lists. Here is an example.
>>> grades = [['Assignment 1', 80], ['Assignment 2', 90], ['Assignment 3', 70]]

To access a nested item, first select the sublist, and then treat the result as a regular list. We can access the items inside the nested lists like this:

>>> grades[0][0]
'Assignment 1'

# ==============================================================================================
Aliasing
Consider the following code:

>>> lst1 = [11, 12, 13, 14, 15, 16, 17]
>>> lst2 = lst1
>>> lst1[-1] = 18
>>> lst2
[11, 12, 13, 14, 15, 16, 18]
After the second statement executes, lst1 and lst2 both refer to the same list. When two variables refer to the same objects, they are aliases. If that list is modified, both of lst1 and lst2 will see the change.

# ==============================================================================================
"""
# Week 5 test

'''
What is the sum of the odd numbers from 1523 through 10503, inclusive? Hint: write a while loop to accumulate the sum and print it. Then copy and paste that sum. For maximum learning, do it with a for loop as well, using range.
'''

def odd_summary_while(num1, num2):
	i = num1
	sum = 0
	while i <= num2:
		sum = sum + i
		i = i + 2
	return sum
	
def odd_summary_for(num1, num2):
	sum = 0
	for i in range(num1, num2 + 1, 2):
		sum = sum + i
	return sum
	
# ==============================================================================================
"""
# ==============================================================================================
for loops over indices

range is typically used in a for loop to iterate over a sequence of numbers. Here are some examples:

# Iterate over the numbers 0, 1, 2, 3, and 4.
for i in range(5):
            
# Iterate over the numbers 2, 3, and 4.
for i in range(2, 5):
            
# Iterate over the numbers 3, 6, 9, 12, 15, and 18.
for i in range(3, 20, 3):
            
# ==============================================================================================
Nested Loops
Bodies of Loops
The bodies of loops can contain any statements, including other loops. When this occurs, this is known as a nested loop.

Here is a nested loop involving 2 for loops:

for i in range(10, 13):
    for j in range(1, 5):
        print(i, j)
               
Here is the output:

10 1
10 2
10 3
10 4
11 1
11 2
11 3
11 4
12 1
12 2
12 3
12 4
Notice that when i is 10, the inner loop executes in its entirety, and only after j has ranged from 1 through 4 is i assigned the value 11.

# ==============================================================================================
Reading Files
Information stored in files can be accessed by a Python program. To get access to the contents of a file, you need to open the file in your program. When you are done using a file, you should close it.

Python has a built-in function open that can open a file for reading.

The form of open is open(filename, mode), where mode is 'r' (to open for reading), 'w' (to open for writing), or 'a' (to open for appending to what is already in the file).

This opens a file called In Flanders Fields.txt for reading:

flanders_file = open('In Flanders Fields.txt', 'r')

Note that if the file is saved in the same directory as your program, you can simply write the name of the file, as what was done in the above example. However, if it is not saved in the same directory, you must provide the path to it.

To close a file, you write flanders_file.close() .

There are four standard ways to read from a file. Some use these methods:

readline(): read and return the next line from the file, including the newline character (if it exists). Return the empty string if there are no more lines in the file.

readlines(): read and return all lines in a file in a list. The lines include the newline character.

read(): read the whole file as a single string.

The readline approach - When you want to process only part of a file.
file = open(filename, 'r')
# Read lines until we reach the
# place in the file that we want.
line = file.readline()
while we are not at the place we want:
    line = file.readline()
# Now we have reached the section
# of the file we want to process.
line = file.readline()
while we are not at the end of the section:
    process the line
    line = file.readline()
flanders_file.close()

The for line in file approach - When you want to process every line in the file one at a time.
file = open(filename, 'r')
for line in file:
    process the line
file.close()

The read approach - When you want to read the whole file at once and use it as a single string.
file = open(filename, 'r')
contents = file.read()
now process contents
file.close()

The readlines approach - When you want to examine each line of a file by index.
file = open(filename, 'r')
# Get the contents as a list of strings.
contents_list = file.readlines()
process contents_list using indexing to
access particular lines from the file
file.close()

# ==============================================================================================
Writing To A File Within A Python Program
In order to write to a file, we use file.write(str). This method writes a string to a file. Method write works like Python's print function, except that it does not add a newline character.

File dialogs
Module tkinter has a submodule called filedialog. We import it like this:
import tkinter.filedialog

Function askopenfilename asks the user to select a file to open:
tkinter.filedialog.askopenfilename()

This function returns the full path to the file, so we can use that when we call function open to open that file.
from_filename = tkinter.filedialog.askopenfilename()

Function asksaveasfilename asks the user to select a file to save to, and provides a warning if the file already exists.
to_filename = tkinter.filedialog.asksaveasfilename()

# ==============================================================================================
Tuples
Tuples are immutable sequences: they cannot be modified. Tuples and lists have much in common, but lists are mutable sequences: they can be modified.

Tuples use parentheses instead of square brackets:

lst = ['a', 3, -0.2]
tup = ('a', 3, -0.2)
Once created, items in lists and tuples are accessed using the same notation:
>>> lst[0]
'a'
>>> tup[0]
'a'
Slicing can be used with both:
>>> lst[:2]
['a', 3]
>>> tup[:2]
('a', 3)
Tuples cannot be modified:
>>> tup[0] = 'b'
TypeError: 'tuple' object does not support item assignment

Tuples have fewer methods than lists. In fact, the only regular methods are count and index. The rest of the list methods are not available for tuple because they modify the object, and tuples, being immutable, cannot be modified.

# ==============================================================================================
Type dict
Another way to store collections of data is using Python's dictionary type: dict.

The general form of a dictionary is:
{key1: value1, key2: value2, ..., keyN: valueN}

Keys must be unique. Values may be duplicated. For example:
asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}

In the example above, the keys are unique: 'A1', 'A2' and 'A3'. The values are not unique: 80, 90 and 90.

Dictionaries are mutable: they can be modified. There are a series of operations and methods you can apply to dictionaries which are outlined below.

object in dict - Checks whether object is a key in dict:
>>> asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}
>>> 'A1' in asn_to_grade
True
>>> 80 in asn_to_grade
False

len(dict) - Returns the number of keys in dict:
>>> asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}
>>> len(asn_to_grade)
3

del dict[key] - Removes a key and its associated value from dict:
>>> asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}
>>> del asn_to_grade['A1']
>>> asn_to_grade
{'A3': 90, 'A2': 90}

dict[key] = value - If key does not exist in dict, adds key and its associated value to dict. If key exists in dict, updates dict by setting the value associated with key to value.	
>>> asn_to_grade = {'A1' : 80, 'A2': 90, 'A3' : 90}
>>> asn_to_grade['A4'] = 70
>>> asn_to_grade
{'A1': 80, 'A3': 90, 'A2': 90, 'A4': 70}

Dictionaries are unordered. That is, the order the key-value pairs are added to the dictionary has no effect on the order in which they are accessed.

A dictionary can be empty. For example:
d = {}

A dictionary can have keys of different types. For example, one key can be of type int and another of type str:
d = {'apple': 1, 3: 4}

The keys of a dictionary must be immutable. Therefore, lists, dictionary and other mutable types cannot be used as keys. The following results in an error:
d[[1, 2]] = 'banana'

Since lists are mutable, they cannot be keys. Instead, to use a sequence as a key, type tuple can be used:
d[(1, 2)] = 'banana'


Switching Keys and Values

Dictionaries have keys that are unique and each key has a value associated with it. For example, here is a dictionary mapping fruit to their colours:
fruit_to_colour = {'watermelon': 'green', 'pomegranate': 'red',
'peach': 'orange', 'cherry': 'red', 'pear': 'green',
'banana': 'yellow', 'plum': 'purple', 'orange': 'orange'}

To invert the dictionary, that is, switch the mapping to be colours to fruit, here is one approach:
>>> colour_to_fruit = {}
>>> for fruit in fruit_to_colour:
    colour = fruit_to_colour[fruit]
    colour_to_fruit[colour] = fruit

>>> colour_to_fruit
{'orange': 'orange', 'purple': 'plum', 'green': 'pear', 'yellow': 'banana', 'red': 'pomegranate'}

The resulting dictionary is missing some fruit. This happens since colours, which are keys, are unique so later assignments using the same colour replace earlier entries. A way to remedy this is to map colours to a list of fruit.

For the example above, we need to consider two cases when adding a colour and a fruit to the dictionary:
 - If the colour is not a key in the dictionary, add it with its value being a single element a list consisting of the fruit.
 - If the colour is already a key, append the fruit to the list of fruit associated with that key.
>>> colour_to_fruit = {}
>>> for fruit in fruit_to_colour:
    # What colour is the fruit?
    colour = fruit_to_colour[fruit]
    if not (colour in colour_to_fruit):
        colour_to_fruit[colour] = [fruit]
    else:
        colour_to_fruit[colour].append(fruit)

>>> colour_to_fruit
{'orange': ['peach', 'orange'], 'purple': ['plum'], 'green': ['watermelon', 'pear'], 'yellow': ['banana'], 'red': ['cherry', 'pomegranate']}

# ==============================================================================================
"""