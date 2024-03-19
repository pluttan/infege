from itertools import combinations

mas = [int(i) for i in open("27/27(17)kab&1.txt")]
m = k = 0
for a, b in combinations(mas, 2):
    if abs(a - b) % 36 == 0 and (a % 13 == 0 or b % 13 == 0):
        m = max(abs(a - b), m)
        k += 1
print(k, m)
