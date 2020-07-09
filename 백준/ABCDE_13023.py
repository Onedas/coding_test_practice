N, M = map(int, input().split())
d={i:[] for i in range(N)}

state = False
def dfs(node, count, visited):
	global state
	if state:
		return

	if count == 5:
		state = True
		return
	
	for next_node in d[node]:
		if next_node not in visited:
			dfs(next_node, count+1, visited + [next_node])

for i in range(M):
	a,b = map(int, input().split())
	d[a].append(b)
	d[b].append(a)

for i in range(M):
	dfs(i, 1, [i])

if state:
	print(1)
else:
	print(0)