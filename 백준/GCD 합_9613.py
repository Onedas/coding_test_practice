def gcd(a,b):
	while b!=0:
		r = a%b
		a = b
		b = r
	return a

T = int(input())
for t in range(T):
	test_case = list(map(int,input().split()))
	n = test_case[0]
	nums = test_case[1:]

	S = 0
	for i,a in enumerate(nums[:-1]):
		for b in nums[i+1:]:
			S+=gcd(a,b)
	print(S)

