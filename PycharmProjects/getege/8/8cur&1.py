from itertools import product

k = 0
for s in product("kompege", repeat=6):
    s = "".join(s)
    if s[0] in "oe" and \
            s[-1] in "oe" and \
            s[1] not in "oe" and \
            s[2] not in "oe" and \
            s[3] not in "oe" and \
            s[4] not in "oe": k += 1
print(k)
