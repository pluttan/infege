from itertools import *
k=0
q=[]
for a,b,c,d,e,f,g,h in permutations("mimicria",r=8):
    q.append(a+b+c+d+e+f+g+h)
print(len(q),len(set(q)))