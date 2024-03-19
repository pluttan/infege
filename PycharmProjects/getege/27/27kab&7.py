mas = [int(i) for i in open("27/27Bkab&7.txt")][1:]
m = 10000000000000000000000000
for i in range(len(mas)):
    for q in range(i, len(mas)):
        if abs(sum(mas[i:q])) % 2077 == 0:
            m = min(sum(mas[i:q + 1]), m)
print(m)