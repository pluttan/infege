from itertools import product

k = 0
for s in product("01234", repeat=6):
    if s[-1] not in "34" and s[0] not in "01":
        k += 1
print(k)
