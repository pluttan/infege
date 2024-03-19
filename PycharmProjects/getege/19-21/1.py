# def f(a, b, c, m):
#     if (a * b) >= 63: return c % 2 == m % 2
#     if c == m: return 0
#
#     h = [f(a + 1, b, c + 1, m), f(a * 2, b, c + 1, m),
#          f(a, b + 1, c + 1, m), f(a, b * 2, c + 1, m)]
#     return all(h) if c % 2 == m % 2 else any(h)
#
#
# for s in range(1, 32):
#     for m in range(5):
#         if f(2, s, 0, m):
#             if m == 4: print(m, s)
#             break

# for i in range(9, 10):
#     x = i
#     a = 3 * x + 23
#     b = 3 * x - 17
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     if a == 10: print(i)

# f = lambda c, e: 0 if c > e or c == 30 else \
#     1 if c == e else \
#         f(c + 1, e) + f(c * 3, e) + f(c * 4, e)
# print(f(2, 15) * f(15, 100))

print(max(map(len, open("24.txt").readline().replace("PR", "P R").replace("RP", "R P").split())))

# for x in range(800000, 10 ** 23):
#     dl = [d for d in range(2, int(x ** 0.5) + 1) if x%d==0];
#     dl += [x // d for d in dl];
#     dl = sorted(list(set(dl)))
#     if (dl[0] + dl[-1]) % 138 == 0:
#         print(x, dl[0] + dl[-1])

mas = [int(i) for i in open("27-B.txt")][1:]
k = 0
for t in range(1, 21):
    for i in range(len(mas) - t):
        q = sum(mas[i:i + t])
        if q % 39 == 0: k += 1
print(k)
