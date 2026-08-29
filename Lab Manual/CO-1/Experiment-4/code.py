from itertools import permutations

words = ["SEND", "MORE"]
result = "MONEY"

letters = set("SENDMORY")
for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))

    if d['S'] == 0 or d['M'] == 0:
        continue

    def num(w):
        return int(''.join(str(d[c]) for c in w))

    if num("SEND") + num("MORE") == num("MONEY"):
        print(d)
        break
