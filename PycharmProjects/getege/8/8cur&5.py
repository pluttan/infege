from itertools import permutations

k = 0
for s in permutations("probnik", 7):
    s = "".join(s)
    if s[0] in "prbnk" and \
            s[-1] in "prbnk" and \
            s.count("oi") == 0 and \
            s.count("io") == 0: k += 1
print(k)
