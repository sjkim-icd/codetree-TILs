cnt_n = 0
sum_n = 0
for _ in range(10):
    n = int(input())
    if 0 <= n <= 200:
        cnt_n += 1
        sum_n += n
    else:
        pass

avg = sum_n/cnt_n
print(sum_n, f"{avg:.1f}")