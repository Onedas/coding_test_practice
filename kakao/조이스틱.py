import sys
def solution(name):
    answer = 0
    v_list=[]
    visited=[]
    length=len(name)

    for i in range(length):
        answer+=min(ord(name[i])-ord('A'),ord('Z')+1-ord(name[i]))
        if name[i]!='A':
            v_list.append(i)

    start=0
    while True:
        if len(v_list)==len(visited):
            break
        d=[cal_distance(start,j,length) if not(j in visited) else sys.maxsize for j in v_list]
        answer+=min(d)
        next=v_list[d.index(min(d))]
        visited.append(next)
        start=next

    return answer

def cal_distance(i,j,length):
    return min(abs(j-i),length-j+i)


print(solution('JEROEN'))
print(solution('JAN'))
# print(solution('ABAAAAAAN'))
print(solution('AAACAN'))


# print(ord('A'))
# print(ord('Z'))