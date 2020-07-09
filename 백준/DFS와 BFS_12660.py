N,M,V=map(int,input().split())
g={n+1:[] for n in range(N)}
for m in range(M):
	a,b = map(int,input().split())
	g[a].append(b)
	g[b].append(a)

def bfs(graph, start):
	visited = []
	queue = [start]
	while queue:
		node = queue.pop()
		if node not in visited:
			visited.append(node)
			queue.extend(reversed(sorted(g[node])))

	return visited

def dfs(graph, start):
	visited =[]
	stack = [start]
	while stack:
		node = stack.pop(0)
		if node not in visited:
			visited.append(node)
			stack.extend(sorted(g[node]))

	return visited

print(*bfs(g,V))
print(*dfs(g,V))