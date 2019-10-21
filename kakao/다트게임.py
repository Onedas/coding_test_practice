def solution(dartResult):
    answer=0

    a=[]
    state=''
    for s in dartResult:
        state += s
        if s=='#' or s=='*':
            a[-1]+=state
            state=''
        elif not (s.isnumeric()):
            a.append(state)
            state=''

    answer_ = []
    for a_ in a:
        for a__ in a_:
            if a__.isnumeric():
                score=int(a__)
            elif a__=='S':
                score**=1
            elif a__=='D':
                score**=2
            elif a__=='T':
                score**=3
            elif a__=='#':
                score*=-1
                if len(answer_)>0:
                    answer_[-1]*=-1
            elif a__=='*':
                score*=2
                answer_*=2
        answer_.append(score)
        score=0
        answer=sum(answer_)

    return answer


if __name__ =="__main__":
    dartResult='1S2D*3T'
    print(solution(dartResult))
