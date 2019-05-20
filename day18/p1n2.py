from itertools import product


STEPS = 100
    

def get_change(row, col):
    light = grid[row][col]
    on = 0
    
    for neighbor in product((1,-1,0), repeat=2):
        if neighbor == (0,0):
            continue
        
        neighbor_row, neighbor_col = neighbor
        if 0 <= row + neighbor_row < len(grid):
            y = row + neighbor_row
        else:
            continue

        if 0 <= col + neighbor_col < len(grid):
            x = col + neighbor_col
        else:
            continue
        
        on += grid[y][x]

    if light:
        return 1 if on in (2,3) else 0
    else:
        return 1 if on == 3 else 0
    

with open('clue.txt') as f:
    start = [[1 if light == '#' else 0 for light in line] for line in f.read().splitlines()]

grid = start

for step in range(STEPS):
    new_grid = []
    for i, row in enumerate(grid):
        new_grid.append([])
        for j,  _ in enumerate(row):
            new_grid[-1].append(get_change(i, j))

    grid = new_grid

print('Part 1:', sum(sum(row) for row in grid))

grid = start

for step in range(STEPS):
    grid[0][0] = 1
    grid[0][-1] = 1
    grid[-1][0] = 1
    grid[-1][-1] = 1
    new_grid = []
    for i, row in enumerate(grid):
        new_grid.append([])
        for j, _ in enumerate(row):
            new_grid[-1].append(get_change(i, j))

    grid = new_grid

grid[0][0] = 1
grid[0][-1] = 1
grid[-1][0] = 1
grid[-1][-1] = 1

print('Part 2:', sum(sum(row) for row in grid))
