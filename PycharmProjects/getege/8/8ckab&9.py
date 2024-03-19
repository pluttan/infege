def f(x):
    k=""
    while x!=0:
        k+=str(x%5)
        x//=5
    return k[::-1]
k=0
for i in range(1,10000000000):
    s=f(i)
    if len(s)==6 and s[-1]!="3" and s[-1]!="4" and s[0]!="1":k+=1
    print(k)