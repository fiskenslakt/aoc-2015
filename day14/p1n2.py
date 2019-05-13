import re

from collections import defaultdict
from operator import itemgetter


SECONDS = 2503 # duration of race

with open('clue.txt') as f:
    descriptions = f.read().splitlines()

p = re.compile(r'(\w+).+?(\d+).+?(\d+).+?(\d+)')
reindeer = defaultdict(dict)

for description in descriptions:
    deer, speed, duration, rest = p.search(description).groups()
    reindeer[deer].update(
        speed=int(speed),
        duration=int(duration),
        rest=int(rest),
        traveled=0,
        elapsed=0,
        rested=0,
        points=0,
    )

# simulate each second of race
for _ in range(SECONDS):
    # iterate through each deer's stats
    for deer in reindeer.values():
        # if deer can move, add speed to traveled
        # to simulate the distance gained from that second
        if deer['elapsed'] < deer['duration']:
            deer['traveled'] += deer['speed']
            deer['elapsed'] += 1
        # deer is resting so increment rest value
        elif deer['rested'] < deer['rest']:
            deer['rested'] += 1
        # rest is finished, reset rest value
        # deer must move in this second
        # so reset elapsed to 1 and
        # add speed to traveled
        else:
            deer['elapsed'] = 1
            deer['rested'] = 0
            deer['traveled'] += deer['speed']

    # increment points for all deer that are
    # currently in the lead (accounts for ties)
    lead = max(reindeer.values(), key=itemgetter('traveled'))
    for deer in reindeer.values():
        if deer['traveled'] == lead['traveled']:
            deer['points'] += 1

# deer that traveled the farthest
# by the end of the race
fastest_deer = max(reindeer, key=lambda d: reindeer[d]['traveled'])
distance = reindeer[fastest_deer]['traveled']
print(f'Part 1: {fastest_deer} traveled {distance} km')

# deer that was most often in the lead
most_points_deer = max(reindeer, key=lambda d: reindeer[d]['points'])
points = reindeer[most_points_deer]['points']
print(f'Part 2: {most_points_deer} won with {points} points')
