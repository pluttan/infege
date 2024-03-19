for i in range(300_000,1_000_000):
    x=i
    dl=[d for d in range(2,int(i**0.5)+2) if i%d==0];dl+=[i//d for d in dl];dl=sorted(list(set(dl)))
    ch=[]
    for i in dl:
        if i%3==0:
            ch+=[i]
    if len(ch)==5:
        print(x,ch[-1])
