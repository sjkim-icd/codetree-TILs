a = int(input()) + 1

for i in range(1,a):
    if (
        ((i % 2 ==0) and (i % 4 != 0)) or
        ((i //8) % 2 ==0) or
        (i % 7 < 4)
        ):
        continue
    print(i, end=' ')