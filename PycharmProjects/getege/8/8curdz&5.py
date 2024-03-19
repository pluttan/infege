from itertools import product

k = 0
for s in product("012345678", repeat=7):
    if s[-1] not in "347":
        if not (s[0] == s[1] == s[2] == s[3]) and \
                not (s[1] == s[2] == s[3] == s[4]) and \
                not (s[2] == s[3] == s[4] == s[5]) and \
                not (s[3] == s[4] == s[5] == s[6]):
            k += 1
print(k)
