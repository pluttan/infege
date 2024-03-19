for a in range(-1,10000000):
        if a==-1:a=""
        q=int("123"+str(a)+"890")
        if q>10**8:break
        if q%27==0:print(q,q//27)