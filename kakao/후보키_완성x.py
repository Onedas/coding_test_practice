combination=[]

def solution(relation):
    answer = 0
    row = len(relation) #data num
    col=len(relation[0]) #attribute
    keys=[]
    result=[]
    for i in range(col):
        dfs(i, col, result)

    # comb= sorted(combination, key=len)
    print(combination)
    return answer

def dfs(curr, size, result):
    if curr==size:
        return
    else:
        result.append(curr)
        combination.append(result[:])

        for i in list(range(curr+1,size+1)):
            dfs(i,size,result)
        result.pop()


if __name__ == '__main__':
    relation=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    answer=solution(relation)
