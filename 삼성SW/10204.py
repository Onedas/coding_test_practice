T = int(input())
for t in range(T):
	N = int(input())
	i = []
	ans = 0

	for n in range(N):
		i.append(list(map(int,input().split())))
	i.sort(key=lambda x:(x[0]+x[1]))
	
	for n in range(N):
		if n%2 == 0:
			ans += i.pop()[0]
		else:
			ans -= i.pop()[1]

	print("#{} {}".format(t+1,ans))
