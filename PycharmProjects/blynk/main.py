from time import time_ns
for i in range(1, 100000):
    print(i)
print(time_ns()//1000000)
# 59818 56237