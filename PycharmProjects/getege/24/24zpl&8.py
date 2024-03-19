x=open("24zpl&8.txt").readline().replace("AB","$")\
    .replace("AC","$")
k = 0
mas = []
for i in x:
    if i != "$":
        mas.append(k)
        k = 0
    else:
        k += 1
print(max(mas))