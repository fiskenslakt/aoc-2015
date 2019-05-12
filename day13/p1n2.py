import re

from collections import defaultdict, namedtuple
from itertools import permutations


def get_optimal_seating():
    optimal_seating = None
    Arrangement = namedtuple('Arrangement', ('seating', 'happiness'))

    # iterate through all possible
    # seating arrangements
    for seating in permutations(graph):
        # convert tuple to list with first element
        # added as the last element to simulate circle
        seating = [*seating, seating[0]]
        happiness = 0
        for p1, p2 in zip(seating, seating[1:]):
            happiness += graph[p1][p2] + graph[p2][p1]

        if optimal_seating is None:
            optimal_seating = Arrangement(seating, happiness)
        elif happiness > optimal_seating.happiness:
            optimal_seating = Arrangement(seating, happiness)

    return optimal_seating


with open('clue.txt') as f:
    invited = f.read().splitlines()

graph = defaultdict(dict)

# graph all possible happiness
# level changes between each person
p = re.compile(r'(\w+).+?(gain|lose)\s(\d+).+?(\w+)\.')
for invite in invited:
    person_a, change, happiness, person_b = p.search(invite).groups()
    if change == 'gain':
        graph[person_a][person_b] = int(happiness)
    else:
        graph[person_a][person_b] = -int(happiness)

optimal_seating = get_optimal_seating()

print('Part 1:', optimal_seating.happiness, '\nArrangement:', optimal_seating.seating)

# add myself to the graph
people = list(graph.keys())
for person in people:
    graph[person]['me'] = 0
    graph['me'][person] = 0

optimal_seating = get_optimal_seating()

print('\nPart 2:', optimal_seating.happiness, '\nArrangement:', optimal_seating.seating)
