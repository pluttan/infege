a="2"*52
while "222" in a or "000" in a:
    if "000" in a:a=a.replace("000","2",1)
    else:a=a.replace("222","02",1)
print(a)