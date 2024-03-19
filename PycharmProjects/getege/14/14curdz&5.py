a = 5 * 7**3 + 2 * 5**2 * 7**2\
    + 3 * 5**3 * 7
k7 = k5 = 0
b = a
while a > 0:
    k7 += a % 7
    a //= 7
while b > 0:
    k5 += b % 5
    b //= 5
print(k7, k5)
