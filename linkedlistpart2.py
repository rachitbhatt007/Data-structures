class Node:
	def __init__(self,data):
		self.data=data
		self.nextnode=None


n=int(input("enter no of nodes"))
l=[]
for i in range(n):
	a=int(input("Enter the value"))
	l.append(Node(a))

for i in range(len(l)):
	print(l[i].data)	

