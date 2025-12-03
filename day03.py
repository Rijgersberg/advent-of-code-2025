from aoc import get_input


def max_joltage(rating, N):
    digits = []
    start = 0
    for n in range(-N, 0):
        substring = rating[start:n+1] if n+1 < 0 else rating[start:]
        
        digit = max(substring)
        digits.append(digit)

        start += substring.find(digit) + 1

    return int(''.join(digits))

ratings = get_input(day=3)
print(sum(max_joltage(rating, N=2) for rating in ratings))
print(sum(max_joltage(rating, N=12) for rating in ratings))
