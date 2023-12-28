n = int(input())

cnt_n = 0
sum_n = 0

for i in range(1,n):
    if n % i == 0 :
        sum_n += i

    else:
        pass
    
if sum_n == n:
    print('P')
else:
    print('N')