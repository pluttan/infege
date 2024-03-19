from itertools import product

k = 0
for s in product("01234", repeat=6):
    if s[0] == "3" and \
            int("".join(s), 5) % 2 == 0:
        k += 1
print(k)
