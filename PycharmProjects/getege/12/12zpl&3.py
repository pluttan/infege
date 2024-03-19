a="23"*30+"1"*30
while "23" in a or "21" in a:
    if "21" in a:a=a.replace("21","11")
    else:a=a.replace("23","21")
print(a.count("1"))