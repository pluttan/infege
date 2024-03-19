from itertools import product

k = 0
for s in product("школа", repeat=3):
    if s.count("к") == 1: k += 1
print(k)
