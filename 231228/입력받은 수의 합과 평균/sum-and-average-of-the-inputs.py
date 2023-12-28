n = int(input())
sum_n = 0
cnt_n = 0
for i in range(n):
    a = int(input())
    sum_n += a
    cnt_n += 1

avg_n = sum_n/cnt_n
print(sum_n, f"{avg_n:.1f}")