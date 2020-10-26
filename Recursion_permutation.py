def permute(s):
	#base case
	if(len(s)==0):
		return s
	if(len(s)==1):
		return s
	else:
		l=[]
		for i in range(len(s)):
			x=s[i]
			xs=s[0:i]+s[i+1:]

			for p in permute(xs):
				l.append(x+p)
		return l
				


print(permute('abc'))
print(permute('xxx'))