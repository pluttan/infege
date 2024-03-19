f=open("24ckab&17.txt").readline().split("D")
m=[]
for a,b,c in zip(f,f[1:],f[2:]):
    m.append(a+b+c+"DD")
print(max(map(len,m)))