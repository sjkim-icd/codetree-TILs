temp = input().split()

a = int(temp[0])
b = int(temp[1])

prod = 1
for i in range(1,b):
    if i % a == 0:
        prod *= i
    else:
        pass

print(prod)