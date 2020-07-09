def permu(arr):
	if len(arr) == 1:
		return [arr]
	else:
		result = []
		for i in arr:
			