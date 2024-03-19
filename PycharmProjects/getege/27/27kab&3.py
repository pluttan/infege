from itertools import combinations

mas = [int(i) for i in open("27/27Bkab&3.txt")][1:]
k = 0
for a, b in combinations(mas, 2):
    if abs(a - b) % 13 == 0 and (a * b) % 2 == 0:
        k += 1
print(k)
