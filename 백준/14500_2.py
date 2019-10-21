import sys
input=sys.stdin.readline
row, col= map(int,input().split())
M=[]
for r in range(row):
    M.append(list(map(int,input().split())))

answer=0
def bar(x,y):
    global answer
    s=0
    if x<=row-4: #l
        s=M[x][y]+M[x+1][y]+M[x+2][y]+M[x+3][y]

    answer=max(s,answer)

def square(x,y):
    global answer
    s=0
    if x<=row-2 and y<=col-2: #ㅁ
        s=M[x][y]+M[x+1][y]+M[x][y+1]+M[x+1][y+1]
    answer = max(s,answer)

def L_shape(x,y):
    global answer
    s=0
    if x<=row-3 and y<=col-2:
        s=M[x][y]+M[x+1][y]+M[x+2][y]+M[x+2][y+1]
    answer= max(s,answer)

def Z_shape(x,y):
    global answer
    s=0
    if x<=row-3 and y<=col-2:
        s=M[x][y]+M[x+1][y]+M[x+1][y+1]+M[x+2][y+1]
    answer = max(s, answer)

def T_shape(x,y):
    global answer
    s=0
    if x<=row-2 and y<=col-3:
        s=M[x][y]+M[x][y+1]+M[x+1][y+1]+M[x][y+2]
    answer=max(s,answer)

def RotateMap_clockwise(row,col,M):
    new_map=[[0]*row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            new_map[j][row-1-i]=M[i][j]

    return col,row,new_map

def FilpMap(row,col,M):
    new_map=[[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            new_map[row-1-i][j]=M[i][j]
    return row,col,new_map


for _ in range(4):
    for i in range(row):
        for j in range(col):
            bar(i,j)
            square(i,j)
            L_shape(i,j)
            Z_shape(i,j)
            T_shape(i,j)
    row,col,M=RotateMap_clockwise(row,col,M)

row,col,M=FilpMap(row,col,M)
for _ in range(4):
    for i in range(row):
        for j in range(col):
            L_shape(i,j)
            Z_shape(i,j)
    row,col,M=RotateMap_clockwise(row,col,M)

print(answer)