def f(c,e,s):
    return 0 if c>e or (c==e and s!=15)\
        else 1 if c==e and s==15\
        else f(c+1,e,s+1)+f(c+5,e,s+1)+f(c*3,e,s+1)
q=set()
for i in range(1000,1025):
    try:
        q.add(f(1,i,0))
        print(len(q))
    except:pass
