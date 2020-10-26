class Node:
	def __init__(self,data):
		self.data=data
		self.nextnode=None
		self.prevnode=None


class Doublyllist():
	def __init__(self):
		self.head=None


	def append(self,data):
		newnode=Node(data)
		if(self.head==None):
			self.head=newnode

		else:
			t=self.head
			while(t.nextnode!=None):
				t=t.nextnode
			t.nextnode=newnode
			newnode.prevnode=t


	def display(self):
		t=self.head
		while(t!=None):
			print(t.data,end=" ")
			t=t.nextnode						
		

d=Doublyllist()
for i in range(5):
	a=int(input())
	d.append(a)
d.display()