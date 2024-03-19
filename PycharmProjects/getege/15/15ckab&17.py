p={2,4,6,8,10,12,14,16,18,20}
q={3,6,9,12,15,18,21,24,27,30}
r={12,24,36,48,60}
a=[]
f=lambda x:(x not in a)<=(((x in p)and(x in q))<=(x in r))
a.extend([x for x in range(1,10000) if not(f(x))])
print(6*18)