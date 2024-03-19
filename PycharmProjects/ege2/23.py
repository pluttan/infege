# 23

from itertools import product, permutations


def m(k):
    return (k + 3), (k + 4), (k + 5)

ko=0
def f(k):
    if k > 42: return False
    if k == 42: return True
    for l in m(k):
        if f(l):
            global ko
            ko+=1
f(22)
print(ko)