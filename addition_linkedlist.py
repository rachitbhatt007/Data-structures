class Node:
	def __init__(self,data):
		self.data=data
		self.nextnode=None


class llist():
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


	def addone(self):
		t=self.head
		prev=self.head
		twoprev=self.head
		while (t.nextnode!=None):
			twoprev=prev
			prev=t
			t=t.nextnode
		if(t.data<9):
			t.data+=1
		elif(t.data==9):
			t.data=0
			if(prev.data<9):
				prev.data+=1
			elif(prev.data==9):
				prev.data=0
				twoprev.data+=1

	def display(self):
		t=self.head
		while(t!=None):
			print(t.data,end=" ")
			t=t.nextnode						
		print()

l=llist()
for i in range(3):
	a=int(input())
	if(len(str(a))==1):
		l.append(a)
	else:
		print("Error Enter Value less than 10")	
		break
l.display()
l.addone()
l.display()	

									