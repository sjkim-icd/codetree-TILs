while True:
    arr = input()
    temp_lst = arr.split()
    # print(temp_lst)
    x = int(temp_lst[0])
    y = int(temp_lst[1])
    z = temp_lst[2]

    xy = x*y
    print(xy)
    
    if z == 'C':
        break