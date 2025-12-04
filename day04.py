from collections import defaultdict

from aoc import get_input


def parse(diagram):
    grid = defaultdict(bool)

    lines = diagram.splitlines()

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '@':
                grid[(r, c)] = True

    R = r + 1
    C = c + 1
    return grid, R, C

def n_neighbors(grid, r, c):
    n = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if not (dr == 0 and dc == 0):
                n += grid[(r+dr, c+dc)]
    return n

def can_be_removed(grid):
    removable = set()
    for r in range(R):
        for c in range(C):
            if grid[(r, c)]:
                if n_neighbors(grid, r, c) < 4:
                    removable.add((r, c))
    return removable


diagram = get_input(day=4, as_list=False)
grid, R, C = parse(diagram)

print(len(can_be_removed(grid)))

removed = None
total = 0
while removed or removed is None:
    removed = can_be_removed(grid)
    total += len(removed)

    for element in removed:
        grid[element] = False
print(total)
