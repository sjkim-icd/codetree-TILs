temp1 = input().split()
temp2 = input().split()

a_math = int(temp1[0])
a_eng = int(temp1[1])
b_math = int(temp2[0])
b_eng = int(temp2[1])


if a_math > b_math:
    print('A')
elif a_math < b_math:
    print('B')
else:
    if a_eng > b_eng:
        print('A')
    elif a_eng < b_eng:
        print('B')