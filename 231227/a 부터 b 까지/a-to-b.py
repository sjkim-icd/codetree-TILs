temp = input().split()
a = int(temp[0])
b = int(temp[1])

for i in range(a,b):

    print(a,end=' ')
    # 조건에 맞춰 수를 변경
    if a % 2 == 1:
        a *= 2
    else:
        a += 3


    if a > b:
        break