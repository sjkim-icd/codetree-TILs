n = int(input()) +1 
cnt_n = 0

for i in range(1,n):
    if ((i % 2 == 0) or 
       (i % 3 == 0) or
       (i % 5 == 0)):
       continue
    cnt_n += 1

print(cnt_n)