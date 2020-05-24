def balancecheck(str):
	l=[]
	for i in str:
		if(i=='{' or i=='(' or i=='['):
			l.append(i)

	for i in str:
		if(i=='}' or i==')' or i==']'):
			l.pop()

	if(len(l)==0):
		print("Balanced")

	else:
		print("not balanced")


balancecheck('((()))')	
balancecheck('({)}')						
balancecheck('[](){([[[]]])}(')
balancecheck('[{{{(())}}}]((()))')		


		