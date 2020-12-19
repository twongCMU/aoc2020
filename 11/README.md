# Day 11

https://adventofcode.com/2020/day/11


I remember this style of problem from last year. The author seems to like these problems with different elements on a grid. Part 1 was pretty straightforward to count the neighbors but I didn't have a good way to generate the list of neighbors to check so I ended up writing 8 if statements to do it. This ended up being hard to debug and I had a couple of comparisons backwards. I also was doing bounds checking wrong by requiring a value to be > 0 instead of >= 0. In looking at my friends' answers afterward I saw that using itertools.product to generate all of the coordinates is the best solution.


Part 2 was not too difficult as I had fortunately broken my code out into functions so it I just had to update how the neighbors were computed using rays. My friends pointed out afterward that it would be more efficient to precompute the list of coordinates that need to be checked rather than redoing that work each time.