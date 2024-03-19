def f(c,e,s):
    return 0 if c>e or (c==e and s!=15)\
        else 1 if c==e and s==15\
        else f(c*2,e,s+1)+f(c*2+1,e,s+1)
q=set()
for i in range(1,10000):
    print(f(1,i,0))