def solution(baseball):
    answer = 0
    plist = [str(i) + str(j) + str(k) for i in range(1, 10) for j in range(1, 10) for k in range(1, 10) if
             i != j and i != k and j != k]

    for p in plist:
        state=0
        for b in baseball:
            if compare(b[0],p)==(b[1],b[2]):
                state+=1

        if state==len(baseball):
            answer+=1

    return answer


def compare(s, o):
    strike = 0
    ball = 0
    s = str(s)
    o = str(o)
    for i in range(3):
        if s[i] == o[i]:
            strike += 1
    if s[0] == o[1] or s[0] == o[2]:
        ball += 1
    if s[1] == o[0] or s[1] == o[2]:
        ball += 1
    if s[2] == o[0] or s[2] == o[1]:
        ball += 1
    return (strike, ball)


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))
