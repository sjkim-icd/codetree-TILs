n = int(input())
sum_n = 0

for _ in range(n):
    a = int(input())
    if (a % 3 == 0) and (a % 2 == 1):
        sum_n += a

print(sum_n)