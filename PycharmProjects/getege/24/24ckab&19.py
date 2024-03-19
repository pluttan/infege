q=f=open("24ckab&19.txt").readline()
f=f.replace("DBAC","$")\
    .replace("A"," ")\
    .replace("B"," ")\
    .replace("C"," ")\
    .replace("D"," ")\
    .replace("E"," ")\
    .replace("F"," ").split()
q=q.split("DBAC")
print(max(map(len,f)),*q)