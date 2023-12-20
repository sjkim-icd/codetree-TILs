temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])

temp_min = min(temp)
temp_max = max(temp)

if (a != temp_min) and (a != temp_max):
    print(a)
elif (b != temp_min) and (b != temp_max):
    print(b)
elif (c != temp_min) and (c != temp_max):
    print(c)