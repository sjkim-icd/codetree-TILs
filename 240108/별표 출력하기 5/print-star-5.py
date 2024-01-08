n = int(input())

# 위에서 아래로 2
for i in range(n,0,-1):
    # 별표 갯수 2
    for j in range(i):
        for j in range(i):
            print('*',end='')
        print(end=' ' )
    
    print()