# k=0
# for i in range(666666999999,10**13,3):
#     if str(i).count("6")==str(i).count("9")==6:k+=1;print(i,k)
from itertools import permutations
k=0
s=set()
print(len(set(permutations("666666999999",r=12))))
# for i in permutations("666666999999",r=12):
#     if i.count("6")==i.count("9")==6:s.add(i);print(len(s),i)
