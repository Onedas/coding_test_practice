def onetwothree(n):
	if n==1:
		return 1
	elif n==2:
		return 2
	elif n==3:
		return 4
	return onetwothree(n-3)+onetwothree(n-2)+onetwothree(n-1)

for t in range(int(input())):
	print(onetwothree(int(input())))