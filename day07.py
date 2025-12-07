from collections import defaultdict
from copy import deepcopy
from itertools import chain

from aoc import get_input


def parse(lines):
    beams = set([lines[0].index('S')])

    splitters = []
    for line in lines[1:]:
        splitters.append(set([i for i, char in enumerate(line) if char == '^']))

    return beams, splitters
    

lines = get_input(day=7)
beams, splitter_rows = parse(lines)

total1 = 0

beams2 = defaultdict(int)  # count how many timelines lead to this beam
beams2[list(beams)[0]] = 1

for splitters in splitter_rows:
    # part 1
    hits = beams.intersection(splitters)

    total1 += len(hits)

    old_beams = beams - hits
    new_beams = set(chain(*[[i-1, i+1] for i in hits]))

    beams = old_beams | new_beams

    # part 2
    for hit in hits:
        beams2[hit-1] += beams2[hit]
        beams2[hit+1] += beams2[hit]
        beams2[hit] = 0

print(total1)
print(sum(v for v in beams2.values()))
