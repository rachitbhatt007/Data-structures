class QueueS:
	def __init__(self):
		self.stack1=[]
		self.stack2=[]

	def isEmpty(self):
		return self.stack1==self.stack2==[]

	def enqueue(self,item):
		self.stack1.append(item)
		

	def dequeue(self):
		for i in range(len(self.stack1),0,-1):
			self.stack2.append(i)

		return self.stack2.pop()

	def display(self):
		return self.stack2


q = QueueS()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(q.display())
print("this is deque",q.dequeue())
print(q.display())





