f=open("27Bckab(2)&11.txt")
q=[int(f.readline()) for i in range(6)][1:]
mas=[int(i) for i in f]
k1=k3=k7=k9=m=0
for x in mas:
    if x % 10 == 1: m += k3
    if x % 10 == 3: m += k1
    if x % 10 == 7: m += k9
    if x % 10 == 9: m += k7
    r=q.pop(0)
    if r % 10 == 1: k1 += 1
    if r % 10 == 3: k3 += 1
    if r % 10 == 7: k7 += 1
    if r % 10 == 9: k9 += 1
    q.append(x)
print(m)