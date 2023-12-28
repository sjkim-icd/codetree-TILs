temp = input().split()

a = int(temp[0])
b = int(temp[1])

prod = 1
for _ in range(b):
    prod *= a

print(prod)