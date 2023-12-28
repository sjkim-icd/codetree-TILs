temp = input().split()

a = int(temp[0])
b = int(temp[1]) + 1 

sum_n = 0
cnt_n = 0

for i in range(a,b):
    if (i % 5 ==0) or  (i % 7 ==0):
        cnt_n += 1
        sum_n += i
    else:
        pass

print(sum_n,f"{sum_n/cnt_n:.1f}")