import math
from collections import Counter
from operator import itemgetter

from aoc import get_input


def parse(lines):
    points = [tuple(map(int, line.split(','))) for line in lines]

    distances = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i+1:]):
            dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

            distances.append((dist, sorted([i, i+j+1])))
    distances.sort(key=itemgetter(0))

    return points, distances


lines = get_input(day=8)
points, distances = parse(lines)

circuits = {i: i for i, point in enumerate(points)}

for t, (dist, (i, j)) in enumerate(distances):
    if circuits[i] != circuits[j]:
        target_id = circuits[j]

        # merge circuits
        for id, cluster_id in circuits.items():
            if cluster_id == target_id:
                circuits[id] = circuits[i]
    
    if t == 1000:
        print(math.prod(size for id, size in Counter([id for id in circuits.values()]).most_common(3)))
 
    if len(set(circuits.values())) == 1:
        print(points[i][0] * points[j][0])
        break
