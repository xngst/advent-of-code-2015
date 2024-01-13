import re


def is_nice(line):
    """
    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    """
    return (
        len(re.findall(r"a|e|i|o|u", line)) >= 3
        and not re.findall(r"ab|cd|pq|xy", line)
        and re.search(r"(\w)\1", line)
    )


def is_nice_2(line):
    """
    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    """
    return re.search(r"(\w)\w\1", line) and re.search(r"(\w\w)\w*\1", line)


with open("input.txt", "r") as f:
    data = f.readlines()

r1 = sum([1 for l in data if is_nice(l)])

r2 = sum([1 for le in data if is_nice_2(l)])

print(f"R1: {r1}")
print(f"R2: {r2}")
