from itertools import combinations


EGGNOG = 150

with open('clue.txt') as f:
    containers = [int(container) for container in f.read().splitlines()]

combos = []
    
for i in range(1, len(containers)+1):
    for combo in combinations(containers, i):
        if sum(combo) == EGGNOG:
            combos.append(combo)

print('Part 1:', len(combos))
print('Part 2:', sum(len(combo) == len(min(combos, key=len)) for combo in combos))
