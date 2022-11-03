# python-principles-challenges


https://pythonprinciples.com/challenges


This is my own version for the challenges showed in python principles web page. Once you solve each one, they show you some solutions. Off course some of them are very fancy but for now those are good enough for me as an exercise.

In addition, there is a lot or room for improvement, for example, the web page accepted my solution for Palindrome or Anagram, but this answer doesn't consider empty space between words. I have my own improved for that version too.

Somebody with basic understanding of Python and Functions shouldn´t have any problem to solve all of them. You should go to the web page an try by yourself before take a look to my files. 

Some examples were really simple an easy for me, so, this is mainly for beginners, although, even at first glance are easy, some of them took me some time. 

Good luck !!!!


Challenge

Capital indexes

Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].



Challenge

Middle letter

Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".




Challenge

Online status

The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
For example, consider the following dictionary:
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.
Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
Your function should return the number of people who are online.



Challenge
Randomness
Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.
Calling the function multiple times should (usually) return different numbers.
For example, calling random_number() some times might first return 42, then 63, then 1.



Challenge

Type check

Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.
For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.



Challenge

Double letters

The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.



Challenge

Adding and removing dots

Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".
If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.
(You may assume that the input to add_dots does not itself contain any dots.)




Challenge
Counting syllables
Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:
"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.
For example, the call count("ho-tel") should return 2.



Challenge

Anagrams

Two strings are anagrams if you can make one from the other by rearranging the letters.
Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.
For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.



Challenge

Flatten a list

Write a function that takes a list of lists and flattens it into a one-dimensional list.
Name your function flatten. It should take a single parameter and return a list.
For example, calling:
flatten([[1, 2], [3, 4]])
Should return the list:
[1, 2, 3, 4]




Challenge

Min-maxing

Define a function named largest_difference that takes a list of numbers as its only parameter.
Your function should compute and return the difference between the largest and smallest number in the list.
For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
You may assume that no numbers are smaller or larger than -100 and 100.




Challenge

Divisible by 3

Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.
For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.



Challenge

Tic tac toe input

Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:


1 X | O | X
 -----------
2 - | - | - 
 -----------
3 O | - | -

  A   B   C




Challenge

Palindrome

A string is a palindrome when it is the same when read backwards.
For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".
Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.




Challenge

Up and down

Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.
For example, calling up_down(5) should return (4, 6).




Challenge

Consecutive zeros

The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:
"1001101000110"
The biggest number of consecutive zeros is 3.
Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.



Challenge

All equal

Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
For example, calling all_equal([1, 1, 1]) should return True.



Challenge
Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.



Challenge

Writing short code

Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.
For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
What makes this tricky is that your function body must only contain a single line of code.



Challenge

Custom zip

The built-in zip function "zips" two lists. Write your own implementation of this function.
Define a function named zap. The function takes two parameters, a and b. These are lists.
Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
You may assume a and b have equal lengths.
If you don't get it, think of a zipper.
For example:
zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
)
Should return:
[(0, 5),
 (1, 6),
 (2, 7),
 (3, 8)]




Challenge

Solution validation

The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.
Write a function named validate that takes code represented as a string as its only parameter.
Your function should check a few things:
•	the code must contain the def keyword
o	otherwise return "missing def"
•	the code must contain the : symbol
o	otherwise return "missing :"
•	the code must contain ( and ) for the parameter list
o	otherwise return "missing paren"
•	the code must not contain ()
o	otherwise return "missing param"
•	the code must contain four spaces for indentation
o	otherwise return "missing indent"
•	the code must contain validate
o	otherwise return "wrong name"
•	the code must contain a return statement
o	otherwise return "missing return"
If all these conditions are satisfied, your code should return True.
Here comes the twist: your solution must return True when validating itself.





Challenge

List xor

Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
Your function must return whether n is exclusively in list1 or list2.
In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.
For example:
list_xor(1, [1, 2, 3], [4, 5, 6]) == True
list_xor(1, [0, 2, 3], [1, 5, 6]) == True
list_xor(1, [1, 2, 3], [1, 5, 6]) == False
list_xor(1, [0, 0, 0], [4, 5, 6]) == False







Challenge

Counting parameters

Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.
For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.




Challenge

Thousands separator

Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousands separator.
For example, calling format_number(1000000) should return "1,000,000".