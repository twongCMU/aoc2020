# Day 18

https://adventofcode.com/2020/day/18


This one stumped me for a bit and I tried a variety of things before settling on one. At first I though about using a stack and parsing tokens because I remember learning that at school, but I couldn't work out on paper how to actually accomplish it! For part 1 I decided that handling an expression with no parenthesis would be easy, so I thought about a way to extract the parenthesis-free expressions. This gave way to the two functions: one to recurse until it found the inner most parenthesis-free expression, then a second one to evaluate it. Once evaluated, the first function would take the answer and substitute the result in place of the expression in the original string.

This ended up making part 2 pretty easy since the puzzle only required updating the second (parenthesis-free evaluation step) function. Furthermore, handling the order of operations could be done using the code to extract and replace the substrings in the first function. I ended up just copy and pasting the extract/replace code from the first function into the second function twice and having the first one handle all additions and the second handle the multiplies. I'm sure it's not the most efficient method, but it worked.