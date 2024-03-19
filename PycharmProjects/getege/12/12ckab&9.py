q=set()
for x in range(1,1000):
    a="5"*x
    while "555" in a or "888" in a:
        a=a.replace("555","8",1)
        a = a.replace("888", "55", 1)
    q.add(a)
print(len(q))