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
        '''inserts a new node after given node
        '''
        if not prev_node:
            print('Previous node is not on the list')
            return

        new_node = Node(data) #create a new node

        new_node.next = prev_node.next # change a next pointer of new node

        prev_node.next = new_node # change a next pointer of prev node

    #Delete methods
    def delete_node(self,key):
        '''deletes a node from a list by its key
        '''
        current_node = self.head 
        #if we want to delete node that is a head node
        if current_node and current_node.data == key: #if the list isn't empty and current_node is that what we seek
            self.head = current_node.next #change the head of list
            current_node = None #removes this node from list
            return
        prev_node = None #if node to be deleted is not head
        while current_node and current_node.data != key:#iterate over list while current_node isn't None and its data isn't key
            prev_node = current_node
            current_node = current_node.next # move the head pointer along
        if current_node is None: #this means that our element isn't present on the list
            return 

        prev_node.next = current_node.next
        current_node = None #delete this node

    def delete_node_at_pos(self,pos):
        '''deletes node at given position
        '''
        current_node = self.head
        if pos == 0: #if we want to delete the head node
            self.head = current_node.next
            current_node = None #removes the head node
            return

        prev_node = None #if we want to delete not a head node we should iterate over the list
        count = 0
        while current_node and count != pos:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        if current_node is None: # the position was greater than the number of elements in the list
            return
        prev_node.next = current_node.next
        current_node = None # deletes node

    def len_iterative(self):
        '''returns the length of the list
        '''
        count = 0
        current_node = self.head
        while current_node: #while current node is valid
            count += 1
            current_node = current_node.next
        return count

llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.print_list()
llist.prepend('E')
print('*')
llist.print_list()
llist.insert_after_node(llist.head.next,'F') # insert "F" node after 'A' node
print('*')
llist.print_list()
print('*')
llist.delete_node('A')
llist.print_list()
llist.delete_node_at_pos(1)
print('*')
llist.print_list()
print('list length',llist.len_iterative())