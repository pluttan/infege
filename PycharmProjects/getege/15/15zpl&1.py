а=lambda x,a: (x%a!=0)<=((x%6==0)<=(x%9!=0))

for a in range(1,1000):
    if all(а(x,a) for x in range(1,10000)):print(a)