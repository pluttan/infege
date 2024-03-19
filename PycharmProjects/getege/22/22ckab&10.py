q=set()
for i1,i2 in zip(range(1,10000000000000),range(1,10000000000000)):
    x,y=i1,i2
    if y>x:
        z=x;x=y;y=z
    a=x;b=y
    while b>0:
        r=a%b;a=b;b=r
    if (a,x)==(13,360763):q.add(y);print(len(q))