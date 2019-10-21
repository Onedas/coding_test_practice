
def solution(m,n,board):
    answer=0
    b=[]
    for s in board:
        s=list(s)
        b.append(s)

    collision=find(m,n,b)
    while len(collision)!=0:
        collision = find(m, n, b)
        for cor in collision:
            idx=cor[0]
            idy=cor[1]
            b[idx][idy]='-'
            answer+=1
        for i in range(m-1):
            for j in range(n-1):
                try:
                    if b[i][j]=='-':
                        b[i][j]=b[i-1][j]
                        b[i-1][j]='-'
                except:
                    pass
    return answer

def find(m,n,board):
    l=set()
    for i in range(m-1):
        for j in range(n-1):
            a=board[i][j]
            b=board[i][j+1]
            c=board[i+1][j]
            d=board[i+1][j+1]
            if a==b==c==d!='-':
                l.add((i,j))
                l.add((i+1,j))
                l.add((i,j+1))
                l.add((i+1,j+1))

    return l
def move(i,j):
    if board[i][j+1]!='-':
        return
    b[i][j+1]==b[i][j]
    move(i,j+1)

if __name__=="__main__":
    m=4
    n=5
    board=['CCBDE','AAADE','AAABF','CCBBF']
    print(solution(m,n,board))