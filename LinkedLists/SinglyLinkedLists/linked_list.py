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
    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None
    #swap by changing the next attribute of node
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.print_list()
# llist.prepend('E')
# print('*')
# llist.print_list()
# llist.insert_after_node(llist.head.next,'F') # insert "F" node after 'A' node
# print('*')
# llist.print_list()
# print('*')
# llist.delete_node('A')
print('swaping nodes B,C')
llist.swap_nodes('B','C')
llist.print_list()