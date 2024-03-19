from itertools import product

k = 0
for s in product("0123456789abcdef", repeat=6):
    predi = "0"
    for i in s:
        if ord(i) < ord(predi):
            break
        predi = i
    else:
        k += 1
print(k)
