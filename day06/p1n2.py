import re


p = re.compile(r'(toggle|on|off)\s(\d+),(\d+).+?(\d+),(\d+)')


def parse_instruction(instruction):
    match = p.search(instruction)
    action = match.group(1)
    start1 = int(match.group(2))
    start2 = int(match.group(3))
    end1 = int(match.group(4))
    end2 = int(match.group(5))

    return action, start1, start2, end1, end2


with open('clue.txt') as f:
    instructions = f.read().splitlines()

light_grid = [[False]*1000 for _ in range(1000)]

for instruction in instructions:
    action, start1, start2, end1, end2 = parse_instruction(instruction)

    for row in range(start2, end2+1):
        for col in range(start1, end1+1):
            if action == 'toggle':
                light_grid[row][col] = not light_grid[row][col]
            elif action == 'on':
                light_grid[row][col] = True
            elif action == 'off':
                light_grid[row][col] = False

print('Part 1:', sum(sum(row) for row in light_grid))

light_grid = [[0]*1000 for _ in range(1000)]

for instruction in instructions:
    action, start1, start2, end1, end2 = parse_instruction(instruction)

    for row in range(start2, end2+1):
        for col in range(start1, end1+1):
            if action == 'toggle':
                light_grid[row][col] += 2
            elif action == 'on':
                light_grid[row][col] += 1
            elif action == 'off':
                light_grid[row][col] -= 1 if light_grid[row][col] else 0

print('Part 2:', sum(sum(row) for row in light_grid))
