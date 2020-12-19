# Day 15

This problem was so devious. The problem is a simple set of rules to implement where, at step N, a number is generated that will be used in step N+1. However, at step N+1, the data is applied to the state of the world at step N-1. I can't think of a time when I've ever encountered anything like this in my work or school and my brain had a hard time understanding this. My code kept updating the state at step N and then at N+1 it would generate the wrong answer. Finally I realized I should keep pending state in step N instead of applying it immediately and only update the state after the computation in step N+1.


Part 2 ended up being trivial and ran with no changes to part 1.