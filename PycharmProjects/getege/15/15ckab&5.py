f=lambda x,a:(a%7==0)and((240%x==0) <= ((a%x!=0) <= (780%x!=0)))
for a in range(1,10000):
    if all(f(x,a) for x in range(1,10000000)):print(a)