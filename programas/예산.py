def solution(d, budget):
    answer = 0
    d.sort(key=lambda x:-x)
    while d:
        budget -= d.pop()
        if budget <0:
            break
        answer +=1
        
    return answer
