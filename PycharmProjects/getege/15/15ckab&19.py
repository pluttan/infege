p = list(range(17, 55))
q = list(range(37, 84))
a = []
f = lambda x: (x in p) <= (((x in q) and not (x in a)) <= (x not in p))
a.extend([x for x in range(1, 10000) if not (f(x))])
print(len(a))
