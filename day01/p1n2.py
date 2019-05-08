with open('clue.txt') as f:
    directions = f.read()

cur_floor = 0
position = None

for i, step in enumerate(directions, 1):
    if step == '(':
        cur_floor += 1
    elif step == ')':
        cur_floor -= 1

    if position is None and cur_floor == -1:
        position = i

print('Part 1:', cur_floor)
print('Part 2:', position)
