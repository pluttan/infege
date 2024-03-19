a="1"*100
while "111" in a or "88888" in a:
    if "111" in a:a=a.replace("111","88")
    else:a=a.replace("88888","8")
print(a)