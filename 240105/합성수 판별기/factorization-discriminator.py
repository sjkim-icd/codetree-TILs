n = int(input())

# 합성수란 약수가 3개 이상
cnt_n  = 0
for i in range(1,n+1):
    if n % i == 0:
        cnt_n += 1
    else:
        pass

if cnt_n > 2:
    print('C')
else:
    print('N')