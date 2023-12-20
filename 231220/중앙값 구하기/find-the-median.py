temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])

temp_min = min(temp)
temp_max = max(temp)


if b<=a<=c or c<=a<=b :
    print(a)
elif b<=c<=a or a<=c<=b:
    print(b)
elif b<=c<=a or a<=c<=b:
    print(c)