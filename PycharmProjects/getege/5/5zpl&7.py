for x in range(1,10000):
    i=bin(x)[2:]
    i=i+"10" if i[-1]=="0" else "1"+i+"01"
    i=int(i,2)
    if i>516:print(x)
