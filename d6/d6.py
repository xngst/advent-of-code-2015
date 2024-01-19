with open("input.txt", "r") as f:
    data = f.readlines()

# PART1


def make_grid(x: int, y: int):
    return [[0 for x_axis in range(x)] for y_axis in range(y)]


def get_coord(instruction: str):
    parts = instruction.split()
    if "on" in instruction or "off" in instruction:
        action = parts[1]
        start_x, start_y = map(int, parts[2].split(","))
        end_x, end_y = map(int, parts[4].split(","))

    if "toggle" in instruction:
        action = parts[0]
        start_x, start_y = map(int, parts[1].split(","))
        end_x, end_y = map(int, parts[3].split(","))

    return action, start_x, start_y, end_x, end_y


grid = make_grid(1000, 1000)

for instruction in data:
    action, start_x, start_y, end_x, end_y = get_coord(instruction)

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == "on":
                grid[x][y] = 1
            elif action == "off":
                grid[x][y] = 0
            else:
                grid[x][y] = 1 - grid[x][y]

r1 = sum(map(sum, grid))
print(f"R1: {r1}")

# PART2

grid = make_grid(1000, 1000)

for instruction in data:
    action, start_x, start_y, end_x, end_y = get_coord(instruction)

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == "on":
                grid[x][y] = grid[x][y] + 1
            elif action == "off":
                if grid[x][y] <= 0:
                    pass
                else:
                    grid[x][y] = grid[x][y] - 1
            elif action == "toggle":
                grid[x][y] = grid[x][y] + 2

r2 = sum(map(sum, grid))
print(f"R2: {r2}")
