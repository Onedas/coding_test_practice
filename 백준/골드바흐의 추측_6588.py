MAX=1000000
prime=[False for _ in range(MAX+1)]

for i in range(2, MAX+1):
    if i*i > MAX:
        break
    if prime[i] is False:
        for j in range(i*i, MAX+1, i):
            prime[j] = True

while True:
    n= int(input())
    if n ==0:
        break
    
    check=True
    for p1 in range(2,MAX+1):
        if prime[p1] is False:
            p2= n-p1
            
            if prime[p2] is False:
                print("{} = {} + {}".format(n,p1,p2))
                check=False
                break
    if check:
        print("Goldbach's conjecture is wrong.")