a="4"*30+"53"*30
while "53" in a or "43" in a:
    if "43" in a:a=a.replace("43","33")
    else:a=a.replace("53","43")
print(a.count("3"))