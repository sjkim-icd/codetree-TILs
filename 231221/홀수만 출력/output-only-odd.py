temp = input().split()
a = int(temp[0])
b = int(temp[1])

# 주어진 a,b 모두 홀수이므로, 홀수 출력시 +2
for i in range(a,b+1,2):
    print(i,end = ' ')