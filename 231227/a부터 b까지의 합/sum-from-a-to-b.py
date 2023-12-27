temp = input().split()
a = int(temp[0])
b = int(temp[1])

sum_n = 0
for i in range(a,(b+1)):
    sum_n += i

print(sum_n)