for x in range(300_000_001,10_000_000_000):
    dl=[d for d in range(2,int(x**0.5)+1) if x%d==0];dl+=[x//d for d in dl];dl=sorted(list(set(dl)))
    try:print(x,dl[-6])
    except:pass