q={3,6,9,12}
p={1,2,3,4,5,6}
a=[]
f=lambda x:not(not(x in a) and (x in q))or not(x in p)
a.extend([x for x in range(1,10000) if not(f(x))])
print(a)