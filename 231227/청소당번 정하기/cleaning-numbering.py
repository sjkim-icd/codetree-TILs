n = int(input())

clean_1 = 0
clean_2 = 0
clean_3 = 0
for i in range(1,(n+1)):
    if i % 12 == 0:
        clean_3 += 1
    elif i % 6 == 0:
        clean_2 += 1
    elif i % 3 == 0:
        clean_2 += 1    
    elif i % 2 == 0:
            clean_1 += 1

print(clean_1,clean_2,clean_3)