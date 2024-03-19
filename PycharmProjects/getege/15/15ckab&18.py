d = list(range(17, 59))
c = list(range(29, 81))
a = []
f = lambda x: (x in d) <= ((not (x in c) and not (x in a)) <= (x not in d))
a.extend([x for x in range(1, 10000) if not (f(x))])
print(len(a))
