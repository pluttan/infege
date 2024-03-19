for x in range(1,10000000):
    a=4**1014-2**x+12
    k=bin(a).count("0")-1
    if k==2000:print(x)