from itertools import permutations

k = 0
for s in permutations("peskarm", 7):
    s = "".join(s)
    if s[0] != "m" and \
            s.count("me") == 0 and \
            s.count("ma") == 0 and \
            s.count("mr") == 0: k += 1
print(k)
