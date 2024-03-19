f = open("27Ackab(2)&15.txt")
q = [int(f.readline()) for i in range(5)][1:]
zmax = [0] * 137
zmin = [100**21] * 137
mas = [int(i) for i in f]
m = 0
for x in mas:
    if zmax[x % 137]!=0:
        m = max(m,abs(zmax[x % 137] - x))
    if zmin[x % 137]!=100**21:
        m = max(m,abs(zmin[x % 137] - x))
    zmax[q[0] % 137] = max(q[0], zmax[q[0] % 137])
    zmin[q[0] % 137] = min(q[0], zmin[q[0] % 137])
    q.pop(0)
    q.append(x)
print(m)
