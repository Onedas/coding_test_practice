import sys

T = int(input())
for test_case in range(1, T + 1):
    N,A,B = map(int,input().split())
    M = min(A,B)
    m = max(A+B-N,0)
    print("#{} {} {}".format(test_case, min(A,B), max(A+B-N,0)))