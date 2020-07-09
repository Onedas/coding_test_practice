E,S,M = map(int,input().split())
e,s,m = 0,0,0
y = 1
while True:
	if e+1==E and s+1==S and m+1==M:
		print(y)
		break
	y+=1
	e = (e+1)%15
	s = (s+1)%28
	m = (m+1)%19
