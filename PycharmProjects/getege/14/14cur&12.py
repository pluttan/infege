a = 5 * 216**3031 + 4 * 36**3042 - 3 * 6**3053 - 3064
k=0
while a>0:
    k+=a%6
    a//=6
print(k)