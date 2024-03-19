def ispr(x):
    k=0
    for d in range(1,x//2+1):
        if x%d==0:k+=1
        if k>2:return False
    if k==2:return True
    else:return False
for x in range(121_332_132,20_222_021,-1):
    for d in range(2, int(x//2) + 1):
        if x % d == 0:
            if ispr(d):
                if d>999:
                    print(x,d)
                break


