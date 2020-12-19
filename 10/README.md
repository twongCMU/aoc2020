# Day 10

Part 1 was pretty easy. I sorted the adapters and then made a histogram.


Part 2 was much harder but I enjoyed it. I chose a memoization solution but I hadn't used memoization since I was preparing for job interviews a year prior. It took a bit of time to work out on paper how to actually keep track of the information I wanted but I'm pretty proud that I was able to work it out without having to get outside help. I got stuck at the very end for quite some time as I used a numpy.uint32 as my counter. Originally I thought I wanted a matrix for my memoization so I used numpy but I ended up removing the matrix but kept the numpy.uint32. As a result my answer for the example was correct but my answer for the final data was wrong. It took quite a bit of time to realize that the hint that there were over a trillion arrangements precisely explained what my bug was and it all worked when I changed my counter to be a regular Python integer.


I also think this is wonderful:

![Elf on a Plane](https://pbs.twimg.com/media/Eo5rKLEXIAcE1UT?format=jpg&name=large)

Source: https://twitter.com/GaryJGrady/status/1337124080579973120