mas=[int(i) for i in open("27_B.txt")][1:]
sta=1000000000
for i in range(len(mas)):
    st=0
    for j in range(len(mas)):
        a = 3*min(abs(i-j), len(mas)-abs(i-j))
        st+=a*mas[j]
    sta=min(sta,st)
    if i%10000==0:print(sta)
print(sta)
