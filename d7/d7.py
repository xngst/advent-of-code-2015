def parse_instruction(line):
    input, output = line.strip().split(" -> ")
    return output, input 


def get_value(wire, circuit):
    if wire.isdigit():
        return int(wire)
    if wire in circuit:
        return circuit[wire]
    instruction = table[wire]
    if instruction.isdigit():
        circuit[wire] = int(instruction)
    elif instruction.startswith("NOT"):
        circuit[wire] = ~ get_value(instruction[4:], circuit) & 0xFFFF
    elif "OR" in instruction:
        wire_1, wire_2 = instruction.split(" OR ")
        circuit[wire] = get_value(wire_1,circuit) | get_value(wire_2,circuit)
    elif "AND" in instruction:
        wire_1, wire_2 = instruction.split(" AND ")
        circuit[wire] = get_value(wire_1,circuit) & get_value(wire_2,circuit)
    elif "LSHIFT" in instruction:
        wire_1, shift_value = instruction.split(" LSHIFT ")
        circuit[wire] = get_value(wire_1,circuit) << int(shift_value)
    elif "RSHIFT" in instruction:
        wire_1, shift_value = instruction.split(" RSHIFT ")
        circuit[wire] = get_value(wire_1,circuit) >> int(shift_value)
    else:
        circuit[wire] = get_value(instruction,circuit)
    return circuit[wire]


with open("input.txt", "r") as f:
    data = f.readlines()

#PART 1
table = dict(parse_instruction(line) for line in data)
print(f"""R1: {get_value("a",circuit={})}""")

#PART 2
table["b"] = str(get_value("a",circuit={}))
print(f"""R2: {get_value("a",circuit={})}""")
