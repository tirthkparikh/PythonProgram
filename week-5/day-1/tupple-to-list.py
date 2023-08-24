# a=(1,2,3,4)
# print(a,type(a))
# a=list(a)
# print(a,type(a))


T = int(input())
for tc in range(T):
	# Read integers a and b.
	(a, b) = map(int, input().split(' '))
	
	ans = a + b
	print(ans)