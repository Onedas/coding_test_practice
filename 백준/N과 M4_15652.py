# N,M = map(int,input().split())
N,M = 5,3
def re(num, count, visited):
	if count == M:
		print(' '.join(map(str,visited)))
		return

	for i in range(num,N+1):
		re(i, count+1, visited+[i])

for i in range(1,N+1):
	re(i, 1, [i])