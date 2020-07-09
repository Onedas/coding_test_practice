def gcd(a,b):
	while b!=0:
		r = a%b
		a = b
		b = r
	return a

def lcm(a,b):
	return a*b//gcd(a,b)

T = int(input())
for t in range(T):
	a,b = map(int,input().split())
	print(lcm(a,b))


