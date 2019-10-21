n = int(input())
m= []
for _ in range(n):
    m.append(map(int,input().split()))
#
# n=4
# m=[[0, 10, 15, 20],
#    [5, 0, 9, 10],
#    [6, 13, 0, 12],
#    [8, 8, 9, 0]
#    ]

answer=float('inf')

import itertools as it
paths = list(it.permutations(range(n)))

for p in paths:
    start_p = list(p[:])
    end_p = list(p[1:])+ [p[0],]

    cal=0
    for i,j in zip(start_p,end_p):
        cal+=m[i][j]
        if cal>answer:
            break

    if cal<answer:
        answer=cal

print(answer)