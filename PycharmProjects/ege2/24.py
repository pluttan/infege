# 24

from itertools import product, permutations

f = open("zadanie24_2.txt").readline().split("L")
m = 0
k = 0
for i in f:
    if i != "":
        m = max(k, m)
        k = 0
    if i == "": k += 1
print(m,f)
