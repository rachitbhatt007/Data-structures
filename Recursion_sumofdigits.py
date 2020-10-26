
def sum(n):
	if(n==0):
		return 0
	else:
		num=n%10
		return num+sum(n//10)


print(sum(467))