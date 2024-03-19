from itertools import combinations

mas = [int(i) for i in open("27/27(17)kab&2.txt")]
k = m = 0
for a, b in combinations(mas, 2):
    if abs(a - b) % 60 == 0:
        k += 1
        m = max(m, abs(a - b))
print(k, m)
