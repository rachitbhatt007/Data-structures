class Deque:
	def __init__(self):
		self.items=[]


	def enquebegin(self,item):
		return self.items.insert(0,item)

	def dequeueend(self):
		return self.items.pop()

	def enqueend(self,item):
		return self.items.append(item)

	def dequeuebegin(self):
		return self.items.pop(0) #or it can be done by self.items.remove(self.items[0])

	def size(self):
		return len(self.items)

	def display(self):
		return self.items

d = Deque()
d.enquebegin(4)
d.enquebegin(5)
print(d.display())
d.dequeuebegin()
print(d.display())