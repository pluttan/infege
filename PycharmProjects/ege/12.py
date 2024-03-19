from itertools import *
from functools import *

def f(x):
    a="1"*x
    while "111"in a:
        a=a.replace("111", "2",1)
        a=a.replace("222", "1",1)
    return (a)
for i in range(1,100):
    print(i,f(i))