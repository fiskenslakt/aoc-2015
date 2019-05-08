import re

from itertools import permutations
from collections import defaultdict, namedtuple


with open('clue.txt') as f:
    distances = f.read().splitlines()

graph = defaultdict(dict)
    
for distance in distances:
    f, t, d = re.search(r'(\w+)\sto\s(\w+).+?(\d+)', distance).groups()
    graph[f][t] = int(d)
    graph[t][f] = int(d)

Route = namedtuple('Route', ('distance','course'))
shortest_route = None
longest_route = None
    
for route in permutations(graph):
    distance = None
    for point_a, point_b in zip(route, route[1:]):
        if distance is None:
            distance = graph[point_a][point_b]
        else:
            distance += graph[point_a][point_b]

    if shortest_route is None:
        shortest_route = Route(distance, route)
    elif distance < shortest_route.distance:
        shortest_route = Route(distance, route)

    if longest_route is None:
        longest_route = Route(distance, route)
    elif distance > longest_route.distance:
        longest_route = Route(distance, route)

print(f'Part 1: {shortest_route.distance} {shortest_route.course}')
print(f'Part 2: {longest_route.distance} {longest_route.course}')
