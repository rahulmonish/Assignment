for i in range(0,1000):
    comp_num = i
    new_num = 0
    while i>0:
        digit = i % 10
        new_num = new_num + digit**3
        i = int(i/10)
    if comp_num == new_num:
        print(comp_num)