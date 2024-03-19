st = open("24zpl&1.txt").readline()
pred = ""
k = 0
mas = []
for i in st:
    if i == pred:
        mas.append(k)
        k = 0
    else:
        k += 1
        pred=i
print(max(mas))
