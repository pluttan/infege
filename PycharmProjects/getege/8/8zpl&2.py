from itertools import product

k = 0
for i in product("0123456789abcdef", repeat=5):
    s = "".join(i)
    if s[0] != "1" and s[0] != "0" and s[-1] not in "02468ace": k += 1
print(k)
