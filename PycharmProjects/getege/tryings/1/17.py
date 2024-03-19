f=[int(x) for x in open("17.txt")]
w=max([x for x in f if x%11==0])
k,m=0,100000000000
for a,b in zip(f,f[1:]):
    if a>w or b>w:
        k+=1
        m=min(m,a+b)
print(k,m)