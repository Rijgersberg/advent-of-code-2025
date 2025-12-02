from aoc import get_input


def parse(input):
    ranges = []
    for text_range in input.split(','):
        start_end = text_range.split('-')
        start = int(start_end[0])
        end = int(start_end[1])
        ranges.append(range(start, end+1))
    return ranges

def valid1(id):
    id = str(id)
    L = len(id)
    if L < 2 or L % 2 == 1:
        return True
    
    left_half = id[:L//2]
    right_half = id[L//2:]

    return left_half != right_half

def valid2(id):
    id = str(id)
    L = len(id)
    if L < 2:
        return True
     
    for l in range(1, L//2 + 1):  # length of pattern to test
        repeated_digits = id[:l]
        for p in range(0, L, l):
            if id[p:p+l] != repeated_digits:
                break  # not invalid for this length of pattern
        else:
            return False # invalid
    return True  # found not invalid for every length of pattern


ranges = parse(get_input(day=2, as_list=False))
total1 = 0
total2 = 0
for r in ranges:
    for i in r:
        if not valid1(i):
            total1 += i
        if not valid2(i):
            total2 += i
print(total1)
print(total2)
