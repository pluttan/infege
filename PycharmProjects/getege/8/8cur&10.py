from itertools import product

k = 0
for s in product("питоняга", repeat=8):
    s = "".join(s)
    if s[0] not in "иояа" and \
            s.count("ио") == 0 and \
            s.count("ои") == 0 and \
            s.count("ия") == 0 and \
            s.count("яи") == 0 and \
            s.count("иа") == 0 and \
            s.count("аи") == 0 and \
            s.count("оя") == 0 and \
            s.count("яо") == 0 and \
            s.count("оа") == 0 and \
            s.count("ао") == 0 and \
            s.count("яа") == 0 and \
            s.count("ая") == 0: k += 1
print(k)
