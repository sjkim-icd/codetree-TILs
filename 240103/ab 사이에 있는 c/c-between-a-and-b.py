temp_lst = input().split()
a = int(temp_lst[0])
b =  int(temp_lst[1])
c = int(temp_lst[2])

satis_yn = False
for i in range(a,b+1):
    if i  % c == 0:
        satis_yn = True

if satis_yn == True:
    print('YES')
else:
    print('NO')