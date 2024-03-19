from itertools import product

k = 0
for s in product("krot", repeat=6):
    if s.count("t") == 1: k += 1
print(*s, sep="")
