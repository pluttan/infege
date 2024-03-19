f=[int(q) for q in open("17ckab&5.txt") if hex(int(q))[-1]=="b" and int(q)%7==0 and int(q)%6!=0 and int(q)%13!=0 and int(q)%19!=0]
print(sum(f),len(f))