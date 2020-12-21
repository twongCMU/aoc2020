#!/usr/bin/python3

import math
import re
from collections import defaultdict
import numpy as np
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

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
for a in allergens:
    for one_ingredient in ingredients.keys():
        seen_in_all = True
        for food in allergens_to_ingredients[a]:
            if one_ingredient not in food:
                #print(str(one_ingredient) + " not in food ingredient list " + str(food))
                seen_in_all = False
                break
        if seen_in_all:
            print("is an allergen " + one_ingredient)
            ingredients[one_ingredient] = 0
            
for i,v in ingredients.items():
    if v != 0:
        print("ingredient is ok " + str(i) + " for " + str(v))
print(str(sum(ingredients.values())))
