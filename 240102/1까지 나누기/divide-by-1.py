n = int(input())
cnt_n = 0
n_n = n
for i in range(1,n+1):
    n_n = n_n // i 
    cnt_n += 1
    if n_n <= 1:
        break

print(cnt_n)