for x in range(1,100):
    i=bin(x)[2:]
    i=i+bin(sum(map(int,list(i))))[2:] if i[-1]=="0" else "1"+i+"00"
    i=int(i,2)
    if i>215:print(x)