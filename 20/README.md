# Day 20

Part 1 was great. The problem sounded intimidating but, after misreading the submission requirement on day 9 I have been much more careful to read what they want as an answer before starting to work. This turned out well as I noticed they specifically asked for the corners of the image and I realized the shortcut in that the corners are the only tiles in the image that have only 2 neighbors. I completed part 1 quickly enough for a globa rank of 180, my best result so far! I was still 3 minutes off of making it to the leaderboard, unfortunately.


The shortcut in part 1 was a relief becuase I knew that recreating the original image would be a nightmare. Part 2's puzzle was exactly that nightmare. Recreating the image by doing edge detection and requiring rotations and flips seemed like a straightforward problem with no shortcuts. At various points I considered simply printing out the data tiles, manually rearranging them, then typing them back in to do the monster detection.


In the end my solution is just to fix one of the corners in the top left then check every tile in every orientation to see what fits in the next opening, working to the right then down. Each subsequent tile is dependent on matching the edge to the top and left. There was a lot of code and a lot of data to keep track of and I lost significant time to off by one errors, removing the edges incorrectly, and having minor bugs in certain rotations and flips.


Back in day 12 (the boat waypoints) I had an issue where I tracked the waypoint's absolute location rather than the relative location to the boat which made the problem much harder. I had a similar thing in this problem where part 1 was simplified by only working with the edges and I painfully manually implemented rotate and flip computations that was time consuming and also bug-prone. In the final part I realized it was much easier to stuff everything into numpy matrices and use the numpy rotate and flip functions. I think it would have simplified everything including part 1 if I had done that all the way through.


Part 2 took me over 6 hours, going to bed at 4am, but I still got a rank of 1881. Such a low rank after so much time suggests that the problem was difficult for everyone. There were leaderboard points available over an hour after the puzzle release.