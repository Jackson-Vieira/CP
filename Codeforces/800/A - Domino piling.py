m,n = [int(i) for i in input().split()]
a  = m*n
if a%2 == 0:
	print(a//2)
else:
	print((a-1)//2)