k=0
for i in range(1,10000000):
    x=i
    a,b=0,0
    while x>0:
        a+=1
        if x%2!=0:b+=1
        x//=2
    if(a,b)==(16,14):k+=1;print(k)