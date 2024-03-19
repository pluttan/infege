from itertools import combinations

mas = sorted([int(i) for i in \
    open("27/27Akab&6.txt")][1:])[:1000]
m = 1000000
for a, b, c in combinations(mas, 3):
    if (a + b + c) % 11 == 0:
        m = min(m, sum([a, b, c]))
print(m)