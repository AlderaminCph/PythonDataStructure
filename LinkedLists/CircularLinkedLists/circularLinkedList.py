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
        ''' appends a new node to the and of the list
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

cllist = CircularLinkedList()
cllist.append('C')
cllist.append('D')
cllist.prepend('B')
cllist.prepend('A')
cllist.remove('B')
cllist.print_list()


