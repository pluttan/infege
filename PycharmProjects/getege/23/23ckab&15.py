def f(c,e):
    return 0 if c>e\
        else 1 if c==e\
        else f(c+1,e)+f(int("".join([str(int(i)+1 if i!="9" else i) for i in str(c)])),e)
print(f(25,51))