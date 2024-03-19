# 17

from itertools import product, permutations

f = list(map(int, open("17.txt").readlines()))
m = 0
k = 0
for x in range(len(f)-1):
    for y in range(x+1,len(f)):
        s = f[x] + f[y]
        if s % 8 == 0:
            m = max(m, s)
            k += 1
print(k,m)