temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])

if a == min(a,b,c):
    print(1, end = ' ') 
else:
    print(0, end = ' ')

if a == b == c:
    print(1)
else:
    print(0)