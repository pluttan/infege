for x in range(1,100):
    i=bin(x)[2:]
    i+=i[-1]
    i+="1" if sum(int(q) for q in i)%2==1 else "0"
    i += "1" if sum(int(q) for q in i) % 2 == 1 else "0"
    if int(i,2)>130:print(int(i,2),x)