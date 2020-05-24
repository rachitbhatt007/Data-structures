class Queue:
	def __init__(self):
		self.items=[]


	def isEmpty(self):
		return self.items==[]

	def enqueue(self,item):
			return self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

q= Queue()
print(q.isEmpty())
q.enqueue(23)
q.enqueue(24)
q.enqueue("mymy")
print(q.size())
q.dequeue()
print(q.size())



					