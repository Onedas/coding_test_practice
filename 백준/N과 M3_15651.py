N,M = map(int,input().split())

def re(count, visited):
	if count == M:
		print(' '.join(map(str,visited)))
		return

	for i in range(1,N+1):
		re(count+1, visited+[i])

for i in range(1,N+1):
	re(1, [i])