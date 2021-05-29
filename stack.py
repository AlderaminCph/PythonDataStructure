'''
Stack Data Structure
'''
class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item) #will append item to the stack

	def pop(self):
		return self.items.pop() #will return the top element of the stack

	def is_empty(self):
		return self.items == [] # will check if the stack is empty

	def peek(self):
		if not self.is_empty(): # will return the top element of the stack
			return self.items[-1]

	def get_stack(self): #will return the stack
		return self.items