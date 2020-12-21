#!/usr/bin/python3

from collections import defaultdict
import sys

allergens = {}
ingredients = defaultdict(int)
allergens_to_ingredients = defaultdict(list) # allergen name to lists where each entry is a list of ingredients from one food
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        v = v[:-1] # remove trailing close paren
        (ing, contains) = v.split(" (contains ")
        ing_list = ing.split(" ")
        contains_list = contains.split(", ")
        for c in contains_list:
            allergens[c] = 1
            allergens_to_ingredients[c].append(ing_list.copy())
        for one_ing in ing_list:
            ingredients[one_ing]+=1

count =0
#print(str(allergens_to_ingredients))
#print("ingredients" + str(ingredients.keys()))
ingredients_to_allergens = defaultdict(list)
for a in allergens:
    for one_ingredient in ingredients.keys():
        seen_in_all = True
        for food in allergens_to_ingredients[a]:
            if one_ingredient not in food:
                #print(str(one_ingredient) + " not in food ingredient list " + str(food))
                seen_in_all = False
                break
        if seen_in_all:
            ingredients[one_ingredient] = 0
            ingredients_to_allergens[one_ingredient].append(a)

print(str(ingredients_to_allergens))
final = {}
while len(ingredients_to_allergens.keys()):
    to_remove = None
    for i in ingredients_to_allergens.keys():
        if len(ingredients_to_allergens[i]) == 1:
            print("removing " + str(i) + ":" + str(ingredients_to_allergens[i]))
            to_remove = i
            break
    final[to_remove] = ingredients_to_allergens[to_remove][0]
    del ingredients_to_allergens[to_remove]
    for i in ingredients_to_allergens.keys():
        if final[to_remove] in ingredients_to_allergens[i]:
            ingredients_to_allergens[i].remove(final[to_remove])
    print("now " + str(ingredients_to_allergens))

print(str(final))

for k in sorted(final.keys(), key=lambda v:final[v]):
    sys.stdout.write(k+",")
print("")
