f=open("24ckab(2)&12.txt").readline()
q=0
m=[]
while q!=len(f):
    if f[q]=="A":
        o=""
        while f[q] != "F" and q!=len(f)-1:
            o+=f[q]
            q+=1
        m.append(o)
    q+=1
k=0
for i in m:
    if 7<=len(i)<=10:k+=1
print(k)