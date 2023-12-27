n = int(input())

year_n = 0
for i in range(1,(n+1)):
    if (i % 100 == 0) and (i % 400 != 0):
        pass 
    elif i % 4 == 0:
        year_n += 1
    
print(year_n)