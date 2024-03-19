mas = [int(i) for i in open("27/27Akab&5.txt")][1:]
k = 0
for i in range(len(mas)):
    for j in range(i + 1, len(mas)):
        if (mas[i] * mas[j]) % 10 == 3 and abs(i - j) > 5:
            k += 1
print(k)
