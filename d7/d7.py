def parse_instruction(line):
    source, target = line.strip().split(" -> ")
    return target, source


def get_value(var):
    if var.isdigit():
        return int(var)
    if var in mem:
        return mem[var]
    s = table[var]
    if s.isdigit():
        mem[var] = int(s)
    elif s.startswith("NOT"):
        mem[var] = ~get_value(s[4:]) & 0xFFFF
    elif "OR" in s:
        s1, s2 = s.split(" OR ")
        mem[var] = get_value(s1) | get_value(s2)
    elif "AND" in s:
        s1, s2 = s.split(" AND ")
        mem[var] = get_value(s1) & get_value(s2)
    elif "LSHIFT" in s:
        s1, d = s.split(" LSHIFT ")
        mem[var] = get_value(s1) << int(d)
    elif "RSHIFT" in s:
        s1, d = s.split(" RSHIFT ")
        mem[var] = get_value(s1) >> int(d)
    else:
        mem[var] = get_value(s)
    return mem[var]


with open("input.txt", "r") as f:
    data = f.readlines()

table = dict(parse_instruction(line) for line in data)
mem = {}

print(f"R1: {get_value('a')}")

table["b"] = str(get_value("a"))
mem = {}
print(f"R2: {get_value('a')}")
