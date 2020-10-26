class Node:
	def __init__(self,data):
		self.data=data
		self.nextnode=None


class llist():
	def __init__(self):
		self.head=None
		self.c=0


	def append(self,data):
		newnode=Node(data)
		if(self.head==None):
			self.head=newnode
			

		else:
			t=self.head
			while(t.nextnode!=None):
				t=t.nextnode
			t.nextnode=newnode

	def reverse(self):
		prev=None
		current=self.head
		nxtnode=None
		while(current!=None):
			nxtnode=current.nextnode
			current.nextnode=prev
			prev=current
			current=nxtnode
		self.head=prev


	def count(self):
		t=self.head
		while(t!=None):
			self.c=self.c+1
			t=t.nextnode
		print("The Count is",self.c) 



	def nthToLastNode(self,n):
		t=self.head
		for i in range(self.c-n):
			t=t.nextnode
		print(t.data)
		

			
	def display(self):
		t=self.head
		while(t!=None):
			print(t.data,end=" ")
			t=t.nextnode						
		print()		

l=llist()
for i in range(5):
	a=int(input("Enter node data \n"))
	l.append(a)

l.display()
l.count()
l.nthToLastNode(2)
			





			