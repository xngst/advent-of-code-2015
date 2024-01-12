import hashlib


def find_first_n_zeros_in_md5(input_string: str, number_of_zeros: int):
    found = False
    number = 0
    while not found:
        key = input_string + str(number).rjust(number_of_zeros, "0")
        m = hashlib.md5()
        m.update(key.encode())
        hexdigest = m.hexdigest()
        if hexdigest[:number_of_zeros] == "0" * number_of_zeros:
            found = True
            return number
        number += 1


input_string = "yzbqklnj"

r1 = find_first_n_zeros_in_md5(input_string, 5)
r2 = find_first_n_zeros_in_md5(input_string, 6)

print(f"R1:{r1}")
print(f"R2:{r2}")
