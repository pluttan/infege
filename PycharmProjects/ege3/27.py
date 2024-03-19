f = list(map(int, open("27-B.txt").readlines()))
mas = f.copy()
mas.sort()
mas=mas[::-1]
smas=[]
for i in range(len(mas)):
    for a in range(i+1,len(mas)):
        for b in range(i+2,len(mas)):
            s=mas[i]+mas[a]+mas[b]
            if s%3==0 and i<100:
                smas.append(s)
                break
            elif i==100:print(max(smas))
