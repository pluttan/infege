b = list(range(18, 53))
c = list(range(16, 42))
a = []
f = lambda x: ((x in b)<=(x in a))and((x not in c) or (x in a))
a.extend([x for x in range(1, 100000) if not (f(x))])
print(len(a))
