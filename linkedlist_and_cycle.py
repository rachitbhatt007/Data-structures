class Node:
	def __init__(self,data):
		self.data=data
		self.nextnode=None

def cycle(node):
	l=[]
	h=node
	i=node
	while(i.nextnode!=None):
		if(i.nextnode==h):
			l.append("Cycle")
			break
		else:
			l.append("NO")
			i=i.nextnode

	if("Cycle" in l):
		print("Cycle")
	else:
		print("No Cycle")			





a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)

a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=a

cycle(a)

print("next node is",a.nextnode.data)

class linkedList():
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

	def count(self):
		t=self.head
		while(t.nextnode!=None):
			c=c+1
		print(c)
		

	def display(self):
		t=self.head
		while(t!=None):
			print(t.data,end=" ")
			t=t.nextnode


	def count(self):
		t=self.head
		while(t!=None):
			self.c=self.c+1
			t=t.nextnode
		print("The Count is",self.c)   


l=linkedList()
n=int(input("Enter no of elements"))
for i in range(n):
	v=int(input())
	l.append(v)
l.count()	
l.display()
				
			


						
					