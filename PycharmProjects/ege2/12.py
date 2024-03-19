#12

from itertools import product,permutations

# НАЧАЛО
#     ПОКА нашлось (10) ИЛИ нашлось (1)
#         ЕСЛИ нашлось (10)
#         ТО заменить (10, 001)
#         ИНАЧЕ заменить (1, 00)
#         КОНЕЦ ЕСЛИ
#     КОНЕЦ ПОКА
# КОНЕЦ

a="1"+"0"*75
while "10" in a or "1" in a:
    if "10" in a:a=a.replace("10","001",1)
    else:a=a.replace("1","00",1)
print(a.count("0"))