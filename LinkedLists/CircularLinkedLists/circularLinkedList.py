''' Circular Linked List Class
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        ''' appends a new node to the end of the list
        '''
        if not self.head: #our list is empty
            self.head = Node(data)
            self.head.next = self.head
        else: #our list is not empty
            new_node = Node(data)
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def prepend(self,data):
        ''' adds new node in the begining of the list
        '''
        new_node = Node(data)
        current_node = self.head
        new_node.next = self.head

        if not self.head: # our list is empty
            new_node.next = new_node
        else: # our list is not empty
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
        self.head = new_node

    def print_list(self):
        ''' prints our list
        '''
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break

    def remove(self,key):
        ''' removes a node from list by key 
        '''
        if self.head.data == key: # if we want to delete the head node
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
        else: # if we want to delete a random node
            current_node = self.head
            prev_node = None
            while current_node.next != self.head:
                prev_node = current_node
                current_node = current_node.next
                if current_node.data == key:
                    prev_node.next = current_node.next
                    current_node = current_node.next

    def __len__(self):
        ''' returns the length of our list
        '''
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

    def split_list(self):
        ''' splits list in two half lists
        '''
        size = len(self)

        if size == 0: #empty list
            return None
        if size == 1: #list contains single node
            return self.head

        mid = size // 2 #general case
        count = 0

        prev_node = None
        current_node = self.head

        while current_node and count < mid: #first half of list
            count += 1
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = self.head

        split_cllist = CircularLinkedList()
        while current_node.next != self.head:
            split_cllist.append(current_node.data)
            current_node = current_node.next
        split_cllist.append(current_node.data)

        self.print_list()
        print('\n')
        split_cllist.print_list()

    def remove_node(self,node):
        ''' removes a node 
        '''
        if self.head == node: # if we want to delete the head node
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
        else: # if we want to delete a random node
            current_node = self.head
            prev_node = None
            while current_node.next != self.head:
                prev_node = current_node
                current_node = current_node.next
                if current_node == node:
                    prev_node.next = current_node.next
                    current_node = current_node.next    

    def josephus_circle(self, step):
        ''' solves the Josephus problem 
        '''
        current_node = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                current_node = current_node.next
                count += 1
            print('REMOVED '+str(current_node.data))
            self.remove_node(current_node)
            current_node = current_node.next

    def is_circular_linked_list(self, input_list):
        ''' checks whether or not the input list is a circular linked list
        '''

        current_node = input_list.head

        while current_node.next:
            current_node = current_node.next
            if current_node.next == input_list.head:
                return True
        return False

import sys  
sys.path.append("/home/nastya/MyGitRepository/PythonDataStructure/LinkedLists/SinglyLinkedLists")  
from linked_list import LinkedList  

llist = LinkedList()
llist.append('C')
llist.append('D')
llist.prepend('B')
llist.prepend('A')
llist.print_list()
print('\n')
cllist = CircularLinkedList()
cllist.append('C')
cllist.append('D')
cllist.prepend('B')
cllist.prepend('A')
cllist.print_list()
print(cllist.is_circular_linked_list(cllist))
print(cllist.is_circular_linked_list(llist))


