a=">"+11*"1"+12*"2"+30*"3"
while ">1" in a or ">2" in a or ">3" in a:
    if ">1" in a:a=a.replace(">1","22>",1)
    if ">2" in a: a = a.replace(">2", "2>", 1)
    if ">3" in a: a = a.replace(">3", "1>", 1)
print(sum(int(q) for q in a.replace(">","")))