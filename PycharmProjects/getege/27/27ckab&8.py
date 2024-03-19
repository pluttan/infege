from itertools import combinations
f = open("27Bckab&8.txt")
mas = [int(q) for q in f][1:]
a50d80 = [0]*80
i50d80 = [0]*80
for i in mas:
    if i > 50000:
        a50d80[i % 80] += 1
    else:
        i50d80[i % 80] += 1
m=a50d80[0]*(a50d80[0]-1)//2+\
  a50d80[0]*i50d80[0]+\
  a50d80[40]*(a50d80[40]-1)//2+\
  a50d80[40]*i50d80[40]
for i in range(1,40):
    m += a50d80[i] * a50d80[80-i]
    m += a50d80[i] * i50d80[80 - i]
    m += i50d80[i] * a50d80[80 - i]
print(m)

#test
k=0
for a,b in combinations(mas,2):
    if (a+b)%80==0 and (a>50000 or b>50000):k+=1
print(k)