temp = input().split()
a = int(temp[0])
b = int(temp[1])

#  두 정수 a, b에 대해 a를 나눠도 나머지가 0이고, b를 나눠도 나머지가 0인 수
cnt_n = 0
for i in range(a,b+1):
    if 1920 % i == 0 and 2880 % i == 0 :
        cnt_n += 1
    else:
        pass
if cnt_n > 0:
    print(1)
else:
    print(0)