f=[int(q) for q in open("17ckab&3.txt") if (int(q)%10==5 or int(q)%10==7) and int(q)%9!=0 and int(q)%11!=0]
print(len(f),min(f)+max(f))