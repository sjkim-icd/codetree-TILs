n = int(input())

cnt_n = 0
while True:

    if n % 2 == 0:
        n = 3*n +1
    else:
        n = 2*n + 2
    
    cnt_n += 1

    if 1000 <= n:
        break


print(cnt_n)