for i in range(1,10000):
    for i2 in range(1,10000):
        x,y=i,i2
        a,b=0,0
        while x*y>0:
            if x>0:a+=1
            if y>0 and y%7>b:b=y%7
            x//=10
            y//=7
        if (a,b)==(4,5):print(i*i2);quit()