for x in range(1_850_000_000,2_000_000_000):
    k=x
    dl=[d for d in range(1,int(k**0.5)+1) if k%d==0];dl+=[k//d for d in dl];dl=sorted(list(set(dl)))
    ch=[]
    for i in dl:
        if i%2==0:ch+=[i]
    if len(ch)%2==1:
        print(x-1_850_000_000,len(ch))
