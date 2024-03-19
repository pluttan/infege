for x in range(350300,10**20):
    dl=[d for d in range(2,int(x**0.5)+1) if x%d==0];dl+=[x//d for d in dl];dl=sorted(list(set(dl)))
    if sum(dl)%13==0 and len(dl)>0:print(x,sum(dl)//13)