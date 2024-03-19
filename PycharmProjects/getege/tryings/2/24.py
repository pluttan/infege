m=open("24.txt").readline()\
    .replace("AB","$")\
    .replace("CB","$")
print(m[:100])
k=0
s=[]
for i in m:
    if i=="$":
        k+=1
    else:
        s.append(k)
        k=0
print(max(s),*s[:10])