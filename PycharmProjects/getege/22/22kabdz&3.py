k=0
for i in range(1,10000000):
    x=i
    l=0
    m=0
    while x>0:
        m+=1
        if x%2!=0:l+=1
        x//=2
    if (l,m)==(4,20):k+=1;print(k)