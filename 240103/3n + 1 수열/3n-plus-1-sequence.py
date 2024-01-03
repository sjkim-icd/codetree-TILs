n = int(input())
cnt_n = 0 
while True:
    if n < 2 :
        break
    

    if n % 2 == 0 :
        n = n//2 
    else:
        n = (3*n + 1)
    cnt_n += 1
    

print(cnt_n)