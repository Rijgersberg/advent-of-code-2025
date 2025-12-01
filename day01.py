from aoc import get_input


instructions = [int(instruction.replace('R', '').replace('L', '-'))
                for instruction in get_input(day=1)]


zeroes = 0
dial = 50
for instruction in instructions:
    dial = (dial + instruction) % 100
    if dial == 0:
        zeroes += 1

print(zeroes)

zeroes = 0
dial = 50
for instruction in instructions:
    step = instruction // abs(instruction)

    for _ in range(abs(instruction)):
        dial = (dial + step) % 100
        if dial == 0:
            zeroes += 1
print(zeroes)
