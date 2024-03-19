f=[int(d) for d in open("17kabdz&4.txt")]
q=min([d for d in f if str(d)[-1]=="4"])+max([d for d in f if str(d)[-1]=="4"])
k,m=0,0
for a,b in zip(f,f[1:]):
    if a+b<q:
        k+=1
        m=max(a+b,m)
print(k,m)