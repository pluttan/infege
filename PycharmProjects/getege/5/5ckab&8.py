for x in range(1,1000):
    i=bin(x)[2:]
    i= "1"+i+"0" if x%2==0 else "11"+i+"11"
    if int(i,2)>52:print(int(i,2))