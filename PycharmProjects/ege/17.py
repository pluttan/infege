from itertools import *
from functools import *

f = list(map(int, open("17.txt").readlines()))
m = f.copy()
k = 0
while k == 0:
    mx = max(m)
    if mx % 3 != 0:
        m.remove(mx)
    else:
        k = mx
kx = 0
km = -10000
for i in range(len(f) - 1):
    if f[i] % 3 == 0 \
            and f[i] != k \
            or f[i + 1] % 3 == 0 \
            and f[i + 1] != k:
        kx += 1
        km = max(km, sum([f[i], f[i + 1]]))
print(kx, km)
