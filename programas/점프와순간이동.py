def solution(n):
    ans = 0  
    ans = dp(n)
    return ans

def decorator_dp(func):
    d={}
    def wrapper(n):
        if n not in d:
            d[n]=func(n)
        return d[n]
    return wrapper

@decorator_dp
def dp(n):
    if n==1:
        return 1
    if n%2 == 0:
        return dp(n/2)
    else:
        return dp(n-1)+1

    
