with open('clue.txt') as f:
    directions = f.read().strip()

houses = {0j:1}
cur_pos = 0j

cardinals = {
    '^': 1j,
    'v': -1j,
    '<': -1,
    '>': 1,
}

for direction in directions:
    cur_pos += cardinals[direction]

    if cur_pos in houses:
        houses[cur_pos] += 1
    else:
        houses[cur_pos] = 1

print('Part 1:', len(houses))

houses = {0j:2}
santa = 0j
robo_santa = 0j

for santa_direction, robo_direction in zip(directions[::2], directions[1::2]):
    santa += cardinals[santa_direction]
    robo_santa += cardinals[robo_direction]

    if santa in houses:
        houses[santa] += 1
    else:
        houses[santa] = 1

    if robo_santa in houses:
        houses[robo_santa] += 1
    else:
        houses[robo_santa] = 1

print('Part 2:', len(houses))
