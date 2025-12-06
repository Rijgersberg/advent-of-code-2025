from aoc import get_input


def parse(input):
    fresh_text, ingredient_text = input.split('\n\n')

    fresh_ranges = []
    for line in fresh_text.splitlines():
        start, end = [int(x) for x in line.split('-')]
        fresh_ranges.append(range(start, end+1))
    
    ingredients = [int(x) for x in ingredient_text.splitlines()]

    return fresh_ranges, ingredients


input = get_input(day=5, as_list=False)

# part 1
fresh_ranges, ingredients = parse(input)
total = 0
for ingredient in ingredients:
    for fresh_range in fresh_ranges:
        if ingredient in fresh_range:
            total += 1
            break
print(total)


# part 2
def merge(range1, range2):
    # non-overlapping
    if range1.stop < range2.start or range1.start > range2.stop:
        raise ValueError('Non-overlapping ranges')
    
    start = min(range1.start, range2.start)
    stop = max(range1.stop, range2.stop)
    return range(start, stop)

def try_a_merge(fresh_ranges):
    for i, fresh_range1 in enumerate(fresh_ranges):
        for fresh_range2 in fresh_ranges[i+1:]:
            try:
                result = merge(fresh_range1, fresh_range2)

                fresh_ranges.remove(fresh_range1)
                fresh_ranges.remove(fresh_range2)
                fresh_ranges.append(result)

                return fresh_ranges
            except ValueError:
                pass
    else:
        return fresh_ranges


n_ranges_prev = float('inf')
while len(fresh_ranges) < n_ranges_prev:
    n_ranges_prev = len(fresh_ranges)
    fresh_ranges = try_a_merge(fresh_ranges)

print(sum(len(fresh_range) for fresh_range in fresh_ranges))
