f=open("27Bckab&17.txt")
mas=[int(i[0]) for i in f]
m=1900000000
for i in range(1,10):
    m=min(m,mas.count(i))
print(m)