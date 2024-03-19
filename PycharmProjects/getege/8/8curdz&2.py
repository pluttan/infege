from itertools import product

k = 0
for s in product("agilmort", repeat=4):
    k += 1
    if "".join(s[-2:]) == "im": print(k, *s)
