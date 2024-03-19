f=open("26ckab(2)&1.txt")
s,m=map(int,f.readline().split())
i,q=sorted([int(x) for x in f]),[]
while sum(q)+i[0]<s:
    for r in range(len(i)-1,0,-1):
        if sum(q) + i[r] < s:
            q+=[i.pop(r)]
            break
    if sum(q) + i[0] < s:
        q+=[i.pop(0)]
print(len(q),q[-1])

