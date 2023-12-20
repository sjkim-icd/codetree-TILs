temp1 = input().split()
temp2 = input().split()
temp3 = input().split()


a_1 = temp1[0]
a_2 = int(temp1[1])
b_1 = temp2[0]
b_2 = int(temp2[1])
c_1 = temp3[0]
c_2 = int(temp3[1])

# 위급상활여부
a_r = 1 if a_1 == 'Y' and a_2>= 37 else 0
b_r = 1 if b_1 == 'Y' and b_2>= 37 else 0
c_r = 1 if c_1 == 'Y' and c_2>= 37 else 0

f_r = a_r + b_r + c_r

if f_r>=2 :
    print('E')
else:
    print('N')