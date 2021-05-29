'''Singly Linked List Data Structure
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None #next pointer

class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next

	# Here are 3 ways how to insert(add) a new node to the list:
	
	def append(self,data):
		'''adds a node to the end of the list
		'''
		new_node = Node(data) #create a new node
		if self.head is None: #if our list is empty
			self.head = new_node
			return
		last_node = self.head # if our list is not empty we start from head and go to the end
		while last_node.next: # while next of node pointer is not equal to None
			last_node = last_node.next #go to the next node
		last_node.next = new_node # here we put the new node

	def prepend(self,data):
		'''adds a node to the head of the list
		'''
		new_node = Node(data) #create new node
		new_node.next = self.head #make it point to the current head of the list
		self.head = new_node #change the head of the list 

	def insert_after_node(self, prev_node, data):
		'''insert a new node after given node
		'''
		if not prev_node:
			print('Previous node is not on the list')
			return

		new_node = Node(data) #create a new node

		new_node.next = prev_node.next # change a next pointer of new node

		prev_node.next = new_node # change a next pointer of prev node

llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.print_list()
llist.prepend('E')
llist.print_list()
llist.insert_after_node(llist.head.next,'F') # insert "F" node after 'A' node
llist.print_list()