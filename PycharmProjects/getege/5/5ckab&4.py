for x in range(1,10000):
    i=bin(x)[2:]
    i+=i[-1]
    i+=str(sum(int(q) for q in i)%2)
    i += str(sum(int(q) for q in i) % 2)
    if int(i,2)>144:print(int(i,2))