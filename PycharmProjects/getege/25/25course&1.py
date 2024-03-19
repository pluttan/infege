for x in range(200_000_000,1_000_000_000):
    dl=[d for d in range(2,int(x**0.5)+1) if x%d==0];dl+=[x//d for d in dl];dl=sorted(list(set(dl)))
    if len(dl)>=5:
        s=dl[0]*dl[1]*dl[2]*dl[3]*dl[4]*dl[5]
        if str(s)[::-1][0]=="1" and x>=s:
            print(s,dl[::-1][0],x,dl)