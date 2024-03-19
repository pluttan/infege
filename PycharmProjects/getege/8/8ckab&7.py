from itertools import *
k=0
for a,b,c,d,e,f,g,h in product("abicolyn",repeat=8):
    s=a+b+c+d+e+f+g+h
    for i in s:
        if s.count(i)!=1:break
    else:
        if "ai" not in s and \
           "ia" not in s and \
           "ao" not in s and \
           "oa" not in s and \
           "ay" not in s and \
           "ya" not in s and \
           "io" not in s and \
           "oi" not in s and \
           "iy" not in s and \
           "yi" not in s and \
           "oy" not in s and \
           "yo" not in s and \
               "bc" not in s and \
               "cb" not in s and \
               "bl" not in s and \
               "lb" not in s and \
               "bn" not in s and \
               "nb" not in s and \
               "cl" not in s and \
               "lc" not in s and \
               "cn" not in s and \
               "nc" not in s and \
               "ln" not in s and \
               "nl" not in s:k+=1
print(k)
