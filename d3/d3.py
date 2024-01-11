with open("input.txt", "r") as f:
    data = f.readline()

# PART1

# ^ (+1,0)
# v (-1,0)
# > (0,+1)
# < (0,-1)


def count_visited_houses(data):
    current = (0, 0)
    visited = set()

    visited.add(current)

    for char in data:
        if char == "^":
            current = (current[0] + 1, current[1])
        if char == "v":
            current = (current[0] - 1, current[1])
        if char == ">":
            current = (current[0], current[1] + 1)
        if char == "<":
            current = (current[0], current[1] - 1)

        visited.add(current)

    return visited


print(f"R1: {len(count_visited_houses(data))}")

# PART2

robo_data = [char for char in data[::2]]

santa_data = [char for char in data[1::2]]

robo_visited = count_visited_houses(robo_data)
santa_visited = count_visited_houses(santa_data)

pair_visited = robo_visited | santa_visited

# one liner using part1 function
print(
    len(
        count_visited_houses([char for char in data[::2]])
        | count_visited_houses([char for char in data[1::2]])
    )
)

print(f"R2: {len(pair_visited)}")
