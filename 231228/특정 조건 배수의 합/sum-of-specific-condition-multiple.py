temp = input().split()

x = int(temp[0])
y = int(temp[1])

a = min(x,y)
b = max(x,y)

sum_n = 0
for i in range(a,b+1):
    if i % 5 == 0:
        sum_n += i
    else:
        pass

print(sum_n)