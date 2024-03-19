from itertools import product

k = 0
for s in product("aimrz", repeat=4):
    k += 1
    if "".join(s) == "ariz":
        print(k)
    print(k, "".join(s))
