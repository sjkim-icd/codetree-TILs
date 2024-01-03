sum_n = 0
cnt_n = 0
while True:
    n = int(input())
    if n <20 or n >29 :
        break
    cnt_n += 1
    sum_n += n


print(f"{sum_n/cnt_n:.2f}")