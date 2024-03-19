for x in range(1,100):
    s=""
    i=x
    while i!=0:
        s+=str(i%3)
        i//=3
    s=s[::-1]

    s+=str(x%3)

    if int(s,3)>99:print(int(s,3))