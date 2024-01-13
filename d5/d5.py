import re


def is_nice(line):
    return (
        len(re.findall(r"a|e|i|o|u", line)) >= 3
        and not re.findall(r"ab|cd|pq|xy", line)
        and re.search(r"(\w)\1", line)
    )


def is_nice_2(line):
    return re.search(r"(\w\w)\w*\1", line) and re.search(r"(\w)\w\1", line)


with open("input.txt", "r") as f:
    data = f.readlines()

r1 = sum([1 for l in data if is_nice(l)])

r2 = sum([1 for le in data if is_nice_2(l)])

print(f"R1: {r1}")
print(f"R2: {r2}")
