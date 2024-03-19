f=open("26ckab(2)&3.txt")
n,s=map(int,f.readline().split())
mas=[int(x) for x in f]
mas.sort(reverse=True)

reis=0
while len(mas)>0:
    reis+=1
    perev=[]
    for i in range(len(mas)):
        if mas[i]+sum(perev)<=s:
            perev+=[mas[i]]
            mas[i]=0
    mas=[x for x in mas if x!=0]
print(reis,sum(perev))