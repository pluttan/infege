from itertools import combinations

mas = [int(i) for i in open("27/27Akab&4.txt")][1:]
k = 0
for a, b in combinations(mas, 2):
    if (a * b) % 65: k += 1
print(k)