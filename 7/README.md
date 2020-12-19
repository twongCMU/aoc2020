# Day 7

Today's puzzle was a bit convoluted in its description but underneath it was not too bad to implement. I stuffed all of the relationships into a dict rather than building some specialized tree which turned out to work well for both parts.


For part 1 I iterated through a queue where for each item I added its enclosing bags to the queue until I reached the top level. For part 2 I did the same thing but in the other direction where I added the child bags to the queue.


I usually prefer iterative solutions over recursive ones because at a previous job we had to be very careful about resource management and recursive solutions could get out of control. We'll see this pattern manifest itself repeatedly in my subsequent solutions.