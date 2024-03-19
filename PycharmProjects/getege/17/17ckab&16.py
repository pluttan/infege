f=[int(q) for q in open("17ckab&16.txt") if int(q)%11==0]
g=[int(q) for q in open("17ckab&16.txt") if int(q)%17==0]
print(len(f),min(f))
print(len(g),max(g))