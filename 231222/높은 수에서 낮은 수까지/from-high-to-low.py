temp = input().split()

a = int(temp[0])
b = int(temp[1])

# 큰 수 x 작은 수 y
if a > b:
    x = a
    y = b
else:
    x = b
    y = a

for i in range(x,y-1,-1):
    print(i,end=' ')