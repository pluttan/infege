# 2 (x → y) ∧ (y ≡ ¬z) ∧ (z ∨ w)

from itertools import product, permutations

for x, y, z, w in product(range(2), repeat=4):
    if ((not x) or y) and (bool(y) == (not z)) and (z or w):
        print(y, w, z, x)
