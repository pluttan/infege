for i in range(1,10000):
    x=bin(i)[2:]
    x="10"+x if x[-1]=="0" else "1"+x+"01"
    x=int(x,2)
    if x>441:print(i)