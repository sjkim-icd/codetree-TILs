n = int(input())

# 3-5, 5-9
for i in range(1,n+1):
    for j in range(i*2-1):
        print('*',end='')
    print()