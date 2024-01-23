with open("input.txt", "r") as f:
    data = [i.strip() for i in f.readlines() if i.strip()]

string_len = 0
decoded_len = 0
encoded_len = 0

for line in data:
    string_len += len(line)
    decoded = bytes(line, "utf-8").decode("unicode_escape")
    encoded = line.replace("\\", "\\\\").replace('"', '\\"')
    decoded_len += len(decoded[1:-1])
    encoded_len += len(encoded) + 2

print(f"R1: {string_len - decoded_len}")
print(f"R2: {encoded_len - string_len}")
