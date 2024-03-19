for i in range(1,1000):
    x=i
    q=7;l=0
    while l<x:l+=q
    l=q-l+x
    if l==q:l=0
    m=(x-l)//q
    if m<l:m,l=l,m
    if (l,m)==(4,8):print(i)