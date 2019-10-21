def solution(str1,str2):
    answer=0
    Set_list=[]
    for str in (str1,str2):
        str=str.upper()
        before=str[0]
        a=[]
        for s in str[1:]:
            a.append(before+s)
            before=s
        Set_list.append(a)

    U,N=[],[]
    for _ in range(len(Set_list[0])):
        i=Set_list[0].pop(0)
        U.append(i)
        if i in Set_list[1]:
            N.append(i)
            Set_list[1].remove(i)
    for _ in range(len(Set_list[1])):
        i=Set_list[1].pop(0)
        U.append(i)

    answer=int(len(N)/len(U)*65536)
    return answer


if __name__=="__main__":
    str1='FRANCE'
    str2='french'
    print(solution(str1,str2))