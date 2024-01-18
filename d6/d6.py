with open("input.txt", "r") as f:
    data = f.readlines()


grid = [[0 for x in range(1000)] for y in range(1000)]


for instruction in data:
    parts = instruction.split()

    if "on" in instruction or "off" in instruction:
        action = parts[1]
        start_x, start_y = map(int, parts[2].split(","))
        end_x, end_y = map(int, parts[4].split(","))

    if "toggle" in instruction:
        action = parts[0]
        start_x, start_y = map(int, parts[1].split(","))
        end_x, end_y = map(int, parts[3].split(","))

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == "on":
                grid[x][y] = 1
            elif action == "off":
                grid[x][y] = 0
            else:
                grid[x][y] = 1 - grid[x][y]


r1 = sum(map(sum, grid))
print(f"R1:{r1}")
