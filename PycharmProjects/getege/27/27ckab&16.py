f=open("27Bckab&16.txt")
mas=[sum(map(int,list(str(int(i))))) for i in f]
m=0
for i in range(1,50):
    m=max(m,mas.count(i))
print(m)