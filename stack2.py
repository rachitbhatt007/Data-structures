class Stack:
	def __init__(self):
		self.item=[]


	def push(self,item):
		return self.item.append(item)

	def pop(self):
		return self.item.pop()

	def isEmpty(self):
		return self.item==[]

	def peek(self):
		return self.item[-1]	

	

s = Stack()
print (s.isEmpty())

(s.push(1))
(s.push('abc'))
(s.push('xyz'))
print(s.peek())
print (s.pop())						