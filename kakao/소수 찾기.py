li=[]
def solution(numbers):
    answer=0
    numbers_list=list(numbers)

    visited=[]
    for i in range(len(numbers_list)):
        permut(i,0,len(numbers_list),visited)

    n=set()
    for p in li:
        s=''
        for p_ in p:
            s+=numbers_list[p_]
        n.add(int(s))
    print(n)
    for s in n:
        if is_prime(s):
            answer+=1
    return answer

def permut(curr,depth,D,visited):
    if depth==D:
        return
    else:
        visited.append(curr)
        li.append(visited[:])

        for i in range(D):
            if not(i in visited):
                permut(i,depth+1,D,visited)
        visited.pop()

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(solution('99'))