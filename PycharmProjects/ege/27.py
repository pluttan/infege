from itertools import *
from functools import *
kolvo=0
f=list(map(int,open("27B.txt").readlines()))
for i in range(len(f)):
    for d in range(len(f)):
        if abs(d-i)>1:
            pair=[f[i],f[d]]
            if sum(pair)%3:
                q=min(i,d)
                r=[]
                for l in range(q,q+abs(d-i)+1):
                    r.append(f[l])
                if sum(r)%2==0:
                    kolvo+=1
print(kolvo)