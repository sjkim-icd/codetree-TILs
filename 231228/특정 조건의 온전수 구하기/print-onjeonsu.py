n = int(input()) + 1

for i in range(1,n):
    if (
        i % 2 ==0 or
        i % 5 ==0 or
        (i % 3 ==0 and i % 9 != 0)):
        continue
    print(i,end=' ')