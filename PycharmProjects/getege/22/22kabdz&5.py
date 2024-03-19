k=0
from itertools import product
for x1,y1 in product(range(1019,100001,1019),repeat=2):
    x,y=x1,y1
    while x!=y:
        if x>y:x-=y
        else:y-=x
    if x==1019:k+=1;print(k)