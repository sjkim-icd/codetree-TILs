n = int(input())

multiple_n = 1
for i in range(1,11):
    multiple_n *= i
    if multiple_n >= n:
        break
print(i)