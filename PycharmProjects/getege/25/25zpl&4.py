for x in range(452021,10**20):
    dl=[d for d in range(2,int(x**0.5)+1) if x%d==0];dl+=[x//d for d in dl];dl=sorted(list(set(dl)))
    if len(dl)>0:
        if (dl[0]+dl[-1])%7==3:
            print(x,dl[0]+dl[-1])