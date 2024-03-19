for x in range(1,1000):
    i=bin(x)[2:]
    i+=str(sum(int(q) for q in i)%2)
    i += str(sum(int(q) for q in i) % 2)
    if int(i,2)<80:print(x)