# Day 23

Part 1 was pretty straight forward: just implement the rules and run it. I used a list and each round had to do some inefficient copies to splice the lists apart and put it all together but for 100 rounds it was easy.


Part 2 really hurt! 1m entries for 10m rounds told me that there was a math trick and that brute force wouldn't work. I spent a few hours trying to find a pattern but the first 10 numbers being shuffled and the rest being ordered made it so hard. I decided to implement a faster brute force to see if I could spot a pattern. From part 1 I knew the memory copies to reassemble the list was too expensive so I implemented a linked list. This way, inserting the 3 removed nodes would be constant time and the only expense was locating the destination cup where the insertion would happen. This ended up being very expensive and it seemed like I was getting only a couple of rounds per second.


On paper I had worked out how the first 7 rounds would look, and I noticed that after the initial rounds, the insert destination was _before_ the current cup. So, I changed my linked list into a doubly linked list and had my search look backwards. The run time went from impossible to returning an answer in 30 seconds. It felt so dirty doing a hack like that!


I saw on Reddit later that one solution was to stuff everything into a dict with the key as the cup ID and the value as the next cup ID. Essentially this is a linked list except that it doesn't require implementing a linked list class. For me it's extra embarrassing because I love using dicts for everything and my linked list class required a lot of debugging.


In my brainstorming I had gotten so close to that solution. I considered using a list where the index into the list was the cup ID and the value was the next cup ID which is exactly the dict solution but I dismissed it thinking that it would be too expensive to search for the values when updating the next cup IDs... but that search doesn't have to happen so I short circuited my own good idea.