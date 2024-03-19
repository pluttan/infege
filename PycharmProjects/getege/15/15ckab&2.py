f=lambda x,a:((x%84!=0)or(x%90!=0))<=(x%a!=0)
for a in range(1,10000):
    if all(f(x,a) for x in range(100000)):print(a)