temp1 = input().split()
temp2 = input().split()

a_age = int(temp1[0])
a_gen = temp1[1]
b_age = int(temp1[0])
b_gen = temp2[1]


if (a_age >=19 and a_gen == 'M' ) or ( b_age  >=19 and  b_gen == 'M'):
    print(1)
else:
    print(0)