mas=[int(i) for i in open("27Bckab(2)&14.txt")]
z=[10**21]*144
m=10**21
for x in mas:
    ost=0 if x%144==0 else 144-x%144
    m=min(m,z[ost]+x)
    z[x%144]=min(x,z[x%144])
print(m)
