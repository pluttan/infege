m = [int(x) for x in open("17.txt")]
w = min([x for x in m if x % 21 == 0])
k = 0
j = 0
for a, b in zip(m, m[1:]):
    if a % w == 0 or b % w == 0:
        k += 1
        j = max(j, a + b)
print(k, j)
