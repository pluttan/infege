for x in range(1,1000):
    i=bin(x)[2:]
    i+="01" if i[-1]=="0" else "10"
    if int(i,2)>81:print(x)