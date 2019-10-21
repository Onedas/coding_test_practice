def solution(brown, red):
    answer = []
    red_list=[[],[]] #가로, 세로
    for i in range(1,red+1):
        if red%i==0:
            if not i in red_list[0]:
                red_list[1].append(i)
                red_list[0].append(red//i)
    for row,col in zip(red_list[0],red_list[1]):
        p_brown=0
        i=-1
        while True:
            if p_brown>=brown:
                break
            else:
                i+=1
                p_brown+=2*(row+i)+2*(col+i)+4

        if p_brown==brown:
            return [row+2*(1+i),col+2*(1+i)]

    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))
print(solution(16,9))
# print(solution(10,2))