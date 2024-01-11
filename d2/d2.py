with open("input.txt", "r") as f:
    data = f.readlines()


def wrapping_paper(dimensions):
    l, w, h = [int(i) for i in dimensions.split("x")]

    smallest_side = min([l * w, w * h, h * l])

    wrapping_paper = 2 * l * w + 2 * w * h + 2 * h * l

    return wrapping_paper + smallest_side


total_wrapping_paper = 0

for line in data:
    total_wrapping_paper += wrapping_paper(line)

print(f"R1: {total_wrapping_paper}")


def ribbon(dimensions):
    shortest_dist = sorted([int(i) for i in dimensions.split("x")])

    bow_ribbon = 1
    for num in shortest_dist:
        bow_ribbon *= num

    a, b = shortest_dist[:2]

    return (a + b) * 2 + bow_ribbon


total_ribbon = 0
for line in data:
    total_ribbon += ribbon(line)

print(f"R2: {total_ribbon}")
