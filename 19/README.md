# Day 19

I had to think about this one for about 30 minutes before I has a good plan of attack. At first I tried to enumerate all possible strings for part 1 since they told us that the matches were finite, but as my code ran I could see that it wasn't making much progress. It then occurred to me that I could filter out a lot of the paths if the substring being generated wasn't going to be useful for matching any of the messages. I think my code keeps way more substrings than necessary but it pruned the tree enough that it could generate the result for part 1 in about 2 seconds.


Luckily, the pruning solution for part 1 worked for part 2 with no changes but the loops in part 2 made it take a bit longer to run, about 25 seconds.


It's interesting to me that my brain almost instantly thought to prune the tree while I was watching the list of all possible matches being generated. This is not something I have ever done at work and I don't think I learned it in school. I feel like I used or read about the technique last year during Advent of Code 2019 and somehow my brain was able to retrieve the idea at exactly the right time. Neat!