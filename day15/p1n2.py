import re

from collections import defaultdict
from itertools import permutations


TEASPOONS = 100


def partitions(n, k, limit=None):
    """Return all partitions that sum to n of size k."""
    if k == 1:
        yield (n,)
        return
    
    if limit is None:
        limit = n
        
    start = (n + k - 1) // k
    stop = min(limit, n - k + 1) + 1
    
    for i in range(start, stop):
        for tail in partitions(n-i, k-1, i):
            yield (i,) + tail


def get_score():
    """Return score of cookie from the
    current state of teaspoon amounts
    for each ingredient.
    """
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0

    for ingredient in ingredients.values():
        capacity += ingredient['capacity'] * ingredient['teaspoons']
        durability += ingredient['durability'] * ingredient['teaspoons']
        flavor += ingredient['flavor'] * ingredient['teaspoons']
        texture += ingredient['texture'] * ingredient['teaspoons']

    if any(stat < 0 for stat in (capacity, durability, flavor, texture)):
        return 0

    return capacity * durability * flavor * texture


def get_calories():
    """Return calorie amount for cookie
    from current state of teaspoon amounts
    for each ingredient.
    """
    calories = 0

    for ingredient in ingredients.values():
        calories += ingredient['calories'] * ingredient['teaspoons']

    return calories


with open('clue.txt') as f:
    ingredients_raw = f.read().splitlines()

p = re.compile(r'(\w+).+?(-?\d+).+?(-?\d+).+?(-?\d+).+?(-?\d+).+?(-?\d+)')
ingredients = defaultdict(dict)

for ingredient in ingredients_raw:
    name, capacity, durability, flavor, texture, calories = p.search(ingredient).groups()
    ingredients[name].update(
        capacity=int(capacity),
        durability=int(durability),
        flavor=int(flavor),
        texture=int(texture),
        calories=int(calories),
    )

best_score = 0    # best overall score
best_calories = 0 # best score with 500 calories

# iterate through every possible sum of 100
# in partitions the size of ingredient amount
for partition in partitions(TEASPOONS, len(ingredients)):
    # iterate through all unique
    # permutations of each sum
    for permutation in set(permutations(partition)):
        # update teaspoon amount for each ingredient
        # according to current permutation
        for teaspoons, ingredient in zip(permutation, ingredients.values()):
            ingredient['teaspoons'] = teaspoons
            
        score = get_score()
        best_score = max(best_score, score)
        
        if get_calories() == 500:
            best_calories = max(best_calories, score)

print('Part 1:', best_score)
print('Part 2:', best_calories)
