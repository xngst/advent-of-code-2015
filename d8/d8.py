with open("input.txt", "r") as f:
    data = [i.strip() for i in f.readlines() if i.strip()]

string_len = decoded_len = encoded_len = 0

for line in data:
    string_len += len(line)
    decoded = bytes(line, "utf-8").decode("unicode_escape")
    encoded = line.replace("\\", "\\\\").replace('"', '\\"')
    decoded_len += len(decoded[1:-1])
    encoded_len += len(encoded) + 2

print(f"R1: {string_len - decoded_len}")
print(f"R2: {encoded_len - string_len}")


#there is a more concise way to calculate day 8
#attribution: mjpieters

from ast import literal_eval

r1 = r2 = 0
for line in data:
    r1 += len(line) - len(literal_eval(line))
    r2 += 2 + line.count('"') + line.count('\\')

print(f"R1: {r1}")
print(f"R2: {r2}")

#Combined to one-liners:
#print(sum([(len(line)-len(literal_eval(line))) for line in data]))
#print(sum([(2+line.count('"')+line.count('\\')) for line in data]))

