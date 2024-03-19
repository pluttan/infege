a=12*"1"+4*"2"
while "11" in a:
    if "112" in a:
        a=a.replace("112","7",1)
    else:a=a.replace("11","3",1)
print(sum(int(q) for q in a))