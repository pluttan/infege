from itertools import product

k = 0
for s in product("vekno", repeat=5):
    k += 1
    if s.count("n") == 2 and s.count("k") == 2: print(k, *s)
