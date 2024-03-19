#15 (4x + 3y < A) ∨ (x ≥ y) ∨ (y ≥ 13)

from itertools import product,permutations

for A in range(1,100):
    for x,y in product(range(1,100),repeat=2):
        if not (4*x+3*y<A or x>=y or y>=13):
            break
    else:
        print(A)