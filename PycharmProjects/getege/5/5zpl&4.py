for x in range(1,100):
    i=bin(x)[2:]
    i="1"+i+"0" if i[-1]=="0" else "1"+i+"1"
    i=int(i,2)
    if i>52:print(i)