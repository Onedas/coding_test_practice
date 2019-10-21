from sys import stdin
input = stdin.readline
from collections import deque


size = int(input())
m = [list(map(int,input().split())) for _ in range(size)]
ans=0
q = deque()

def get(i,j):
    if m[i][j]:
        q.append(m[i][j])
        m[i][j]=0

def merge(i,j,di,dj):
    while q:
        x=q.popleft()
        if not m[i][j]:
            m[i][j] = x
        elif m[i][j] == x:
            m[i][j] = 2*x
            i,j= i+di, j+dj
        else:
            i,j= i+di, j+dj
            m[i][j] = x

def move(k):
    if k==0:
        for j in range(size):
            for i in range(size):
                get(i,j)
            merge(0,j,1,0)
    elif k==1:
        for j in range(size):
            for i in range(size-1, -1, -1):
                get(i,j)
            merge(size-1,j,-1,0)
    elif k==2:
        for i in range(size):
            for j in range(size):
                get(i,j)
            merge(i,0,0,1)

    else:
        for i in range(size):
            for j in range(size-1, -1, -1):
                get(i,j)
            merge(i, size-1, 0, -1)

def solve(cnt):
    global m, ans
    if cnt ==5:
        for i in range(size):
            ans= max(ans, max(m[i]))
        return
    b=[x[:] for x in m]
    for k in range(4):
        move(k)
        solve(cnt+1)
        m=[x[:] for x in b]

if __name__ == "__main__":
    solve(0)
    print(ans)