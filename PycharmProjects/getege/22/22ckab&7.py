for i in range(20,21):
    t=i;c=0;n=0;d=5
    while n!=300:
        n+=t
        t+=d
        c+=1
    if c%2!=0:c+=d
    if c==8:print(i);break