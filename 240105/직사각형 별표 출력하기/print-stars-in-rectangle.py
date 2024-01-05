temp_lst = input().split()
a = int(temp_lst[0])
b = int(temp_lst[1])

for _ in range(a):
    for _ in range(b):
        print('*',end=' ')
    print()