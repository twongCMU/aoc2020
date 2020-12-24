# Day 24

Part 1 was an excellent puzzle. The hexagonal grid threw me for a loop and took a few minutes to figure out how to represent it but once I found the trick this was straightforward and I felt accomplished. Using a regular x,y matrix, I defined East and West as (+2,0) and (-2,0) so that the math would work with North/South East and North/South West. For example, going North East then South East would be (+1,+1) and (-1,+1) for a combined (0,+2) which is just East. There are some unused tiles but that has no adverse effects.


Part 2 was also pretty simple since we've seen Conway's Game of Life twice already, for for that same reason I was not very pleased to see this puzzle. I lost focus while implementing it and I was stymied by extremely an buggy implementation.