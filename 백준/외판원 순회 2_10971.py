n=int(input())
nums = list(map(int,input().split()))
add, sub, multi, division = list(map(int,input().split()))
maxv = -float('inf')
minv = float('inf')

def cal(num, idx, add, sub, multi, division):
	global n, maxv, minv
	if idx == n:
		maxv = max(num, maxv)
		minv = min(num, minv)
		return

	else:
		if add:
			cal(num + nums[idx], idx+1, add-1, sub, multi, division)
		if sub:
			cal(num - nums[idx], idx+1, add, sub-1, multi, division)
		if multi:
			cal(num * nums[idx], idx+1, add, sub, multi-1, division)
		if division:
			cal(num/nums[idx], idx+1, add, sub, multi, division-1)

cal(nums[0], 1, add, sub,multi,division)
print(int(maxv))
print(int(minv))