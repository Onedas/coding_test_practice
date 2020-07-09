def is_PrimeNumber(n):
	if n==1:
		return False
	
	for i in range(2,n):
		if n%i ==0:
			return False
	return True

N=int(input())
nums = list(map(int,input().split()))
count = 0
for n in nums:
	if is_PrimeNumber(n):
		count+=1
print(count)