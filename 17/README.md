# Day 17

https://adventofcode.com/2020/day/17


This problem was pretty simple since we had already done a neighbor counting Conway's Game of Life simulation problem on Day 11. This time it was easier to write because on day 11, in comparing solutions with friends, I learned about using itertools.product to generate the list of neighbors rather than enumerating a long list of if statements.


The main trick to this problem was to move the initial dataset into the center of a workspace so that it could grow in all directions. My solution is a little inefficient because it does computations for every tile in the workspace even if, in early rounds, it is impossible for the outer tiles to be affected and could be skipped. Luckily the dataset is small enough that it doesn't break down. Even with this inefficient processing, the code for part 2's 4-dimensional data completes in about 2.5 minutes.