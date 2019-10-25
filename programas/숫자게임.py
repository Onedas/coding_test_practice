def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    while A:
        a= A.pop()
        if B[-1]> a:
            answer+=1
            B.pop()

    return answer
