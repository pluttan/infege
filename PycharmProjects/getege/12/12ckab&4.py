a="1"*46+"2"*31
while "1111" in a:
    a=a.replace("1111","2",1)
    a=a.replace("222","1",1)
print(a)