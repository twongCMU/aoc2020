# Day 3

I know the puzzle designer likes these kinds of 2d maps with obstacles on them and I had trouble with them at Advent of Code 2019. As a result I was a bit worried to see one show up so early this year. Luckily the problem was not as difficult. It only worries about intersecting trees at each landing position, not the intermediary travel between markers.


The key to part 1 is simply knowing to use modulo. Part 2 required modifying my code from part 1 to handle different rates of movement. The hard part was allowing for dropping down 2 rows at a time so I just hacked in a counter to skip rows.

