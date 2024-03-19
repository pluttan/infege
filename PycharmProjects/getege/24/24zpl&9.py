x=open("24zpl&9.txt").readline().replace("BA","$")\
    .replace("DA","$")
k = 0
mas = []
for i in x:
    if i != "$":
        mas.append(k)
        k = 0
    else:
        k += 1
print(max(mas))