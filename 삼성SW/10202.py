T = int(input())
for t in range(T):
	N = int(input())
	A = input()
	B = input()
	C = input()
	ans = 0
	for a,b,c in zip(A,B,C):
		ans += len(set([a,b,c])

	print("#{} {}".format(t+1, ans))
