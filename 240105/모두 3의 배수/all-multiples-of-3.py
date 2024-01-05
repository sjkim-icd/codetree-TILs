satis_yn = True
for i in range(5):
    n = int(input())
    if n % 3 == 0:
        pass
    else:
        satis_yn = False

if satis_yn == False:
    print(0)
else:
    print(1)