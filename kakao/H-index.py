def solution(citations):
    answer = 0
    for i in range(len(citations)+1):
        num=sum(1 if x>=i else 0 for x in citations)
        if num<i:
            return answer
        answer=i

    return answer

print(solution([3,0,6,1,5]))
print(solution([10,100]))
print(solution([6,6,6,6,6,6]))
print(solution([2,2,2]))