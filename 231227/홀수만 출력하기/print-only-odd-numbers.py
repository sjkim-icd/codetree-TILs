# n = int(input())

# # 첫번째 줄에 n을 받음
# # 두번째줄부터는 n번에 걸쳐 각 정수값을 받기 위해 input for로 호출


# if (n % 3 == 0) and (n % 2 == 1):
#     print(n)
# else:
#     pass

# for i in range(n+1):
#     num = int(input())
#     if (num % 3 == 0) and (num % 2 == 1):
#         print(num)
#     else:
#         pass

n = int(input())
for _ in range(n):
    num = int(input())
    if num % 2 == 1 and num % 3 == 0:
        print(num)