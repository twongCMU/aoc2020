# Day 16

Part 1 was easy to understand but tough to code because there was a lot to keep track of and I confused myself with so many nested loops, but ultimately got the solution in a short amount of time.


Part 2, however, was much more difficult and stumped me for quite a bit. I wasn't sure how to solve the constraint problem to figure out which field matched with which rule. In the end I assumed that the puzzle maker wouldn't make a solution impossibly difficult and assumed that iteratively removing the fields with only a single possible rule would eventually yield the correct result. This turned out to be a valid assumption (and not unreasonable given how other Advent of Code puzzles that tend to be complex often end up with some dataset constructed to have a more simple result).


I read later that the dataset was so well constructed that it each column's possible rules was the same as one other column's but with one additional one. Therefore the fastest solution would have been to sort the columns by number of rules and simply diff the largest two!

