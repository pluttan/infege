from itertools import product
f=lambda x,y,a:(x**2-10*x+16>0)or(y**2-10*y+21>0)or(x*y<2*a)
for a in range(100):
    if all(f(x,y,a) for x,y in product(range(1,1000),repeat=2)):print(a)