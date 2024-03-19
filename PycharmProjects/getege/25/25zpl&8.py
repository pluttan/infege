for i in range(9):
    for i2 in range(9):
        if int(f"12345{i}6{i2}8")%17==0:
            print(f"12345{i}6{i2}8",int(f"12345{i}6{i2}8")//17)