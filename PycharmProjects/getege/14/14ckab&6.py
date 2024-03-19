for x in range(1,10000):
    a=4**2015-2**2015+2**x+15
    k=bin(a).count("1")
    if k==500:print(x)