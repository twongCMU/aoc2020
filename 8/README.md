# Day 8

Finally, a CPU emulator problem! I had been eagerly awaiting these problems. My favorite problem from Advent of Code 2019 was the intcode puzzle where we had to write an AI to play Arkanoid. Last year there was a long sequence of puzzles that built on the previous solution and I was looking forward to this again. Sadly, they haven't revisited this problem since (I'm writing this summary on day 19).


Part 1 was pretty straightforward to implement. I had a bug where I named my instruction "noop" instead of the provided "nop".


I used a brute force approach to Part2 (as did most of my friends) and it ran quickly enough. I read about optimizations where cycles are precomputed and validations can quit out early but for the small dataset this wasn't necessary.