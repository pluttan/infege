from itertools import product

k = 0
q = 0
for s in product("чистыйразум", repeat=5):
    s = "".join(s)
    if s.count("й") <= 1: k += 1
    q += 1
print(k, q)
