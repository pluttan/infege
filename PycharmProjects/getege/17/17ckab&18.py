f=[int(q) for q in open("17ckab&18.txt")]
m=[]
for a,b in zip(f,f[1:]):
    if (a%9==0 and b%9!=0 and abs(b)%8==3) or (b%9==0 and a%9!=0 and abs(a)%8==3):
        m.extend([a,b])
print(len(m)//2,max(m))