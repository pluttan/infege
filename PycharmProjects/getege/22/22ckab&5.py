for i in range(1,33):
    for i2 in range(1,10000000):
        x,y=i,i2
        a,b=0,0
        while x>0 or y>0:
            if x>0:a+=1
            if y<0:b+=1
            x//=2
            y//=10
        if (a,b)==(6,7):print(i*i2);quit()