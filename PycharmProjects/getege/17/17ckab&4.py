f=[int(q) for q in open("17ckab&4.txt") if int(q)%13==7 and int(q)%7!=0 and int(q)%11!=0]
print(max(f)-min(f),len(f))