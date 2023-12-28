temp = input().split()
a = int(temp[0])
b = int(temp[1]) +1
prod = 1

for i in range(a,b):
    prod *= i

print(prod)