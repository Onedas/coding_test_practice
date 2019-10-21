def solution(n,lost,reserve):
    answer=0

    li=[1 if n>=i>0 else -1 for i in range(n+2)]
    for i in lost:
        li[i]-=1
    for i in reserve:
        li[i]+=1

    for i in range(n+1):
        if li[i]==0:
            if li[i-1]==2:
                li[i-1]=1
                li[i]=1
            elif li[i+1]==2:
                li[i+1]=1
                li[i]=1

    answer = sum([1 if x>0 else 0 for x in li])
    return answer


print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))
