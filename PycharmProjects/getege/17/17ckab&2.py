f=[int(q) for q in open("17ckab&2.txt") if (int(q)%10==2 or int(q)%10==7) and int(q)%3==0 and int(q)%11==0]
print(len(f),min(f))