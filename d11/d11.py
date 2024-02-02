# attribution: r-sreeram

pw = "cqjxjnds"
rounds = 2

sequence = lambda s: any(
    ord(a) + 2 == ord(b) + 1 == ord(c) for a, b, c in zip(s, s[1:], s[2:])
)
doublets = lambda s: len(set(a for a, b in zip(pw, pw[1:]) if a == b)) > 1

while rounds:
    pw = pw.rstrip("z")
    if pw:
        index, char = next(
            ((i, c) for i, c in enumerate(pw) if c in "ilo"), (-1, pw[-1])
        )
        pw = pw[0:index] + (
            "jmp"[q] if (q := "hkn".find(char)) != -1 else chr(ord(char) + 1)
        )
        pw = pw.ljust(8, "a")
    if sequence(pw) and doublets(pw):
        rounds -= 1
        print(pw)
