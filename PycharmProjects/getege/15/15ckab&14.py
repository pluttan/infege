b,c={1,3,5,7,9,11},{3,6,9,12}
a=set()
for x in range(1,1000):
    if ((x in b)<=((x not in c)))==0:a.add(x)
print(a)