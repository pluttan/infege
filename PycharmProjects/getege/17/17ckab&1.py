f=[int(q) for q in open("17ckab&1.txt") if int(q)%3==0 and int(q)%7!=0 and int(q)%17!=0 and int(q)%19!=0 and int(q)%27!=0]
print(len(f),max(f))
