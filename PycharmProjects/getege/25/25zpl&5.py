for x in range(500000,10**20):
    dl=[d for d in range(2,int(x**0.5)+1) if x%d==0];dl+=[x//d for d in dl];dl=sorted(list(set(dl)))
    for i in dl:
        if i!=8 and i%10==8:
            print(x,i)
            break