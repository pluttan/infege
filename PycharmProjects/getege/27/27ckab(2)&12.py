f = open("27Ackab(2)&12.txt")
q = []
mas = [int(i) for i in f][1:]
m = 0
for x in range(len(mas)):
    for y in q:
        if (mas[x] + y) % 8 != 0:
            m += 1
    q.append(mas[x])
    if len(q) > 7:
        q.pop(0)
print(m)
