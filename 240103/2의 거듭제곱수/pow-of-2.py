n = int(input())

cnt_n = 1
multiple_n = 2

while True:
    n //= 2 
    if n == 1:
        break
    cnt_n += 1

print(cnt_n)