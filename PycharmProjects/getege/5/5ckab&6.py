for x in range(1,1000):
    i=bin(x)[2:]
    i=str(int(i[::-1]))
    if int(i,2)==13 and x<=100:print(x)