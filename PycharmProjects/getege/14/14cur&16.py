a = 11 * 15**65 + 18 * 15**38\
    - 14 * 15**17 + 19 * 15**11+18338
s = set()
while a > 0:
    s.add(a % 15)
    a //= 15
print(len(s))