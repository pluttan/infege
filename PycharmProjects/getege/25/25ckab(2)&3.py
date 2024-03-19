for x in range(154026,154044):
    dl=[d for d in range(1,int(x**0.5)+1) if x%d==0];dl+=[x//d for d in dl];dl=sorted(list(set(dl)))
    if len(dl)==4:print(*dl[2:])