temp = input().split()
a = int(temp[0])
b = int(temp[1])

if a >= 90:
    if b >= 95:
        print(10)
    elif b>=90:
        print(5)
    else:
        print(0)
else:
    print(0)