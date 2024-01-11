with open("input.txt", "r") as f:
    data = f.readline()


def floor_count(data):
    up_count = 0
    down_count = 0

    for i in data:
        if i == "(":
            up_count += 1
        else:
            down_count += 1

    return up_count - down_count


print(f"R1: {floor_count(data)}")
# print(len([i for i in data if i == "("]) - len([i for i in data if i == ")"]))


def enter_basement(data):
    position = 0
    step = 1

    for i in data:
        if i == "(":
            position += 1
        else:
            position -= 1

        if position < 0:
            return step
        else:
            step += 1


print(f"R2: {enter_basement(data)}")
