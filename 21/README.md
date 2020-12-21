# Day 21

Today's problem was much easier than yesterday's. I wonder if they swapped in an easier one after seeing how difficult Day 20 was.


Part 1 wasn't too difficult though I don't completely know if my solution works for the set of rules or if it just happens to work for my dataset. I figured that if any ingredient exists in every single food that has a specific allergen listed, it must be an allergen though I don't necessarily know which one. My code just goes through and deletes ingredients that aren't in every food for a given allergen. This worked but once again I've confirmed that I have good intuition about algorithms and solutions but I'm really bad at quickly writing bug-free code!


Part 2 was a bit of a surprise. The submission criterion is a string and not a number for the first time this year, and I don't remember if that ever happened in Advent of Code 2019. It was pretty easy to reduce my results from part 1 to a set of possible allergens for each ingredient that is known to be an allergen. As in Day 16, I assumed that the possible allergens could be determined by iteratively removing ingredients with only a single possible allergen, then removing that allergen from all other ingredients as a possibility. This worked and luckily did not require solving a more complex constraint problem.