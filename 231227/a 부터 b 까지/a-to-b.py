inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
i = a

# 출력
while i <= b:
	print(i, end=" ")
	if i % 2 == 1:
		i *= 2
	else:
		i += 3