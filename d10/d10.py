def look_and_say(s):
    result = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result += str(count) + s[i]
        i += 1
    return result


def generate_sequence(start, iterations):
    current_sequence = start
    for _ in range(iterations):
        current_sequence = look_and_say(current_sequence)
    return current_sequence


puzzle_input = "1113222113"

r1 = generate_sequence(puzzle_input, 40)
r2 = generate_sequence(r1, 10)

print(f"R1: {len(r1)}")
print(f"R2: {len(r2)}")


# Alternative solution with itertools and functools
# attribution: mjpieters
from itertools import groupby
from functools import reduce


def looksay(digits):
    return "".join([f"{len(list(group))}{d}" for d, group in groupby(digits)])


r1 = reduce(lambda prev, i: looksay(prev), range(40), "1321131112")
r2 = reduce(lambda prev, i: looksay(prev), range(10), res1)

print(f"R2: {len(r2)}")
print(f"R2: {len(r2)}")
