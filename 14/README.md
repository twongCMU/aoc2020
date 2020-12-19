# Day 14

I enjoyed this problem. At its surface it is a pretty simple bitmask problem but the introduction of the X means traditional bitwise operators can't be immediately applied. I solved part 1 by generating two regular bit masks out of the supplied one and applying them to the data.


The second part was more complex and at first I wasn't sure how to approach it. I tried enumerating a list of numbers and then applying the first bit to the first X then the second bit to the second X, and so on, but it was too difficult keeping track of the different indexes. I reworked my code and generated a queue where I repeatedly replaced an X with two new entries 0 and 1 back into the queue until all of the Xs were exhausted. 