for x in range(100,1000):
    i=str(x);i=sorted([int(i[0])*int(i[1]),int(i[1])*int(i[2])]);i=i[1]+i[0]
    if i=="240":print(x)