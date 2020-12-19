# Day 13

https://adventofcode.com/2020/day/13


Part 1 was easy. I just looped multiplying each of the cycle times until they were all just over the required time and took the lowest one.


Part 2 turned out to be extremely difficult and my friends really hated this one. It turns out the bus cycle times were all coprimes so it could be solved trivially using the Chinese Remainder Theorem. None of us knew this and I had to work out a solution separately. My friends hate this kind of 'gotcha' question where knowing the knowing the trick is the difference, like a bad interview question that doesn't actually reveal the ability of the candidate.


However this isn't an interview with a time limit so I actually enjoyed this questionquite a bit because of how I was able to solve it by reasoning out a method. My friends and I all tried the same technique to start which was to just increment time by 1 and check if it was the solution. This would work but would take ages. A friend pointed out that we could increment time by the maximum bus cycle time instead of 1 since the alignment must be a multiple of the bus cycle times. Even though I was incrementing time by 821 each iteration now this was stil not a feasible solution.


Eventually I worked it out by thinking about astronomy and planets. (The Asimov book Nightfall comes to mind). I thought about how space launches to other planets works better at certain times because both planets are aligned well. Earth orbits the sun at a period and, say, Mars orbits the sun at a different period. At some other period which is a multiple of both planets' and therefore at a much longer period than either planet individually, the alignment recurs. From this we can imagine that the alignment of 3 planets at a specific configuration occurs at an even less frequent period than any 2 of those planets but still at a multiple of the times when those 2 are aligned. My code therefore finds bus alignments for an increasing number of buses and increments the period at which it checks by the also increasing period of the larger alignments.


By the time my code finishes it is jumping 3488192519981 units of time per iteration and completes in under 0.1 seconds. There was a hint that the solution is larger than 100000000000000 but rather than risk fumbling a computation I started my time at the offset that the bus with the longest cycle time would have to be at if the initial arrangement were valid. This did not have any noticeable effect on the run time.