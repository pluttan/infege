f= lambda x,a: (x%15!=0 or x%28!=0 or x%a==0) and a>70
for a in range(1,1000):
    if all(f(x,a) for x in range(1,10000)):print(a)