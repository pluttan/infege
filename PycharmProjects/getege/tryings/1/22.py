# k=0
# for i in range(666666999999,10**13,3):
#     if str(i).count("6")==str(i).count("9")==6:k+=1;print(i,k)
from itertools import combinations
print(len(combinations("666666999999",r=12)))