from itertools import *
from functools import *

f=open("26.txt").readlines()
k,mem=map(int,f[0].split())
f.remove(f[0])
f=map(int,f)
zmem=0
vid,ph=[],[]
for i in f:
    if i>=101:vid.append(i)
    else:ph.append(i)
q=0
while zmem<mem:
    if mem/2>zmem:
        zmem+=min(vid)
        vid.remove(min(vid))
        q+=1
    else:
        zmem += min(ph)
        pd=min(ph)
        ph.remove(min(ph))
        q+=1
print(mem-(zmem-pd),q-1)