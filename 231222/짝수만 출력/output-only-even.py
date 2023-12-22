temp = input().split()

a = int(temp[0])
b = int(temp[1])

i = a
while i <=b:
    if i%2==0:
        print(i,end=' ')
        i +=1
    else:
        i +=1