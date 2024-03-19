for i in range(9):
    for i2 in range(9):
        if int(f"1234{i}57{i2}8")%17==0:
            print(f"1234{i}57{i2}8",int(f"1234{i}57{i2}8")//17)