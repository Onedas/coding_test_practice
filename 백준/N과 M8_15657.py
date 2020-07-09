N,M = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()

def re(num, count, visited):
	if count == M:
		print(' '.join(map(str,visited)))
		return
	
	for i in range(num,N+1):
		re(i, count+1, visited+[seq[i-1]])

for i in range(1,N+1):
	re(i, 1, [seq[i-1]])