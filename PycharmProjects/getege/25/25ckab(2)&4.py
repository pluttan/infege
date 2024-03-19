for x in range(150000,10000000):
    dl=[d for d in range(2, int(x**0.5)+1) if x%d==0];dl+=[x//d for d in dl];dl=sorted(list(set(dl)))
    s=sum(dl)
    if s%13==10:print(x,s)