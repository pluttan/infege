# 5

from itertools import product, permutations
k=0

def f(a):
    a = str(a)
    a=[int(a[0]) + int(a[1]), int(a[2]) + int(a[3])]
    a.sort()
    return "".join(list(map(str,a)))
for i in range(1000,10000):
    if f(i) =="616":k+=1
print(k)