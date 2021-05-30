'''Doubly Linked Lists Data Structure
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		''' appends data to the end
		'''
		if self.head == None: #empty list
			new_node = Node(data)
			new_node.prev = None
			self.head = new_node
		else:
			new_node = Node(data)
			current_node = self.head
			while current_node.next:
				current_node = current_node.next
			current_node.next = new_node
			new_node.prev = current_node
			new_node.next = None

	def prepend(self, data):
		''' adds data in front of the list
		'''
		if self.head == None:
			new_node = Node(data)
			new_node.prev = None
			self.head = new_node
		else:
			new_node = Node(data)
			self.head.prev = new_node
			new_node.next = self.head
			self.head = new_node
			new_node.prev = None

	def print_list(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next

dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()
