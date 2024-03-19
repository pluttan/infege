for a in range(10):
    for b in range(10):
        for c in range(10):
            q=int("2"+str(a)+"34"+str(b)+"56"+str(c)+"8")
            if q%151==0:print(q,q//151)