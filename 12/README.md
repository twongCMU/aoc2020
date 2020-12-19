# Day 12

https://adventofcode.com/2020/day/12


Part 1 was easy enough to just maintain a state machine to move the coordinates or direction.


Part 2 took me a long time and I think I will consider this the puzzle that I hated the most at the end of the Calendar. The rotation of the waypoint was too hard for my little brain, and even worse I made the critical mistake of trying to maintain absolute coordinates for it instead of just coordinates relative to the boat. This made the code very buggy and added a layer of complexity to my thought process. An additional issue was that I misunderstood the problem and I tried to maintain the boat direction as well and when I realized that wasn't needed I haphazardly removed it.


What I learned from solving part 2 was that if I'm solving a puzzle the wrong way, I should not be afraid to delete all of the code and start over fresh with a new idea rather than try to hack onto code that was implemented badly.