cnt_n = 0
while True:
    n = int(input())
    if n % 2 == 1:
        pass
    else:
        n_2 = n // 2 
        print(n_2)
        cnt_n += 1
    
    if cnt_n == 3:
        break