N,M= map(int,input().split())
g={n+1:[] for n in range(N)}
for m in range(M):
	u,v = map(int,input().split())
	g[u].append(v)
	g[v].append(u)

def bfs(graph, start):
	visited =set()

	queue=[start]
	while queue:
		node = queue.pop()

		if node not in visited:
			visited.add(node)
			queue.extend(graph[node])

	return visited

visited=set()
result = 0 
for n in range(1,N+1):
	if n not in visited:
		result +=1
		visited = visited | bfs(g,n)
print(result)