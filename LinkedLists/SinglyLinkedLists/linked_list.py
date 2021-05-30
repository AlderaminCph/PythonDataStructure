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
    
    def len_recursive(self,node):
        '''calculate the list length recursively
        '''
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self,key1,key2):
        '''change places two nodes by their keys
        '''
        if key1 == key2:
            return
        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2: # if any of these nodes is None we can't swap them
            return

        # case1: Neither of them are not a head node. This means that they have previous nodes.

        if prev_1: #if node1 has previous node => it's not a head node
            prev_1.next = curr_2
        else: #node1 is the head node
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else: #node2 is the head node
            self.head = curr_1

        curr_1.next,curr_2.next = curr_2.next,curr_1.next #swapping them

    def print_helper(self,node,name):
        if node is None:
            print(name + ': None')
        else:
            print(name + ': ' + node.data)

    #reverse list
    # A->B->C->D->0
    # D->C->B->A->0
    # A<-B<-C<-D<-0

    def reverse_iterative(self):
        prev_node = None
        current_node = self.head

        while  current_node:
            nxt = current_node.next #temporary variable with pointer to the next node
            current_node.next = prev_node
            
            self.print_helper(prev_node,'PREV')
            self.print_helper(current_node,'CURR')
            self.print_helper(nxt,'NEXT')
            print('\n')

            prev_node = current_node
            current_node = nxt

        self.head = prev_node

    def reverse_recursive(self):

        def _reverse_recursive(current_node,prev_node):
            if not current_node: #if we rich the end of the list
                return prev_node
            nxt = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = nxt
            return _reverse_recursive(current_node,prev_node)
        self.head = _reverse_recursive(current_node = self.head,prev_node = None)

    def merge_sorted(self,llist):
        '''merges two sorted lists
        '''
        p = self.head
        q = llist.head
        s = None

        if not p: #this means that the first list doesn't exists
            return q #we return the second sorted list
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s #update list head
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
            if not p:
                s.next = q
            if not q:
                s.next = p
        return new_head

    def remove_duplicates(self):
        '''deletes duplicating values from a list
        '''
        current_node = self.head
        prev_node = None

        dupl_values = {}

        while current_node:
            if current_node.data in dupl_values:
                #Remove node
                prev_node.next = current_node.next
                current_node = None
            else:
                #Have not encountered element before
                dupl_values[current_node.data] =1
                prev_node = current_node
            current_node = prev_node.next

    def print_nth_from_last_1(self,n):

        # Method 1:

        total_length = self.len_iterative()
        current_node = self.head

        while current_node:
            if total_length == n:
                print(current_node.data)
                return current_node
            total_length -= 1
            current_node = current_node.next
            if current_node is None:
                return

    def print_nth_from_last2(self,n):

        # Method 2:

        p = self.head
        q = self.head

        count = 0

        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print(str(n) + ' is greater than the number of nodes in list')

        while p and q:
            p = p.next
            q = q.next
        return p.data

    def count_occurances_iterative(self, data):
        # 1->2->1->3->4->1->1
        # Number of ones is 4
        current_node = self.head
        count = 0
        while current_node:
            if current_node.data == data:
                count+=1
            current_node = current_node.next
        return count

    def count_occurances_recursivly(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurances_recursivly(node.next, data)
        else:
            return self.count_occurances_recursivly(node.next, data)

    def rotate(self, k):
        # 1->2->3->4->5->6->none
        #          p     q
        # k = 4
        # 5 -> 6 -> 1 -> 2 -> 3 -> 4 -> None
        #pnext q ->head->          p -> None

        p = self.head
        q = self.head

        count = 0
        prev_node = None

        while p and count < k:
            prev_node = p
            p = p.next
            q = q.next
            count += 1
        p = prev_node

        while q:
            prev_node = q
            q = q.next
        q = prev_node
        q.next = self.head
        self.head = p.next
        p.next = None

    def is_pailndrome_1(self):
        '''Example palindromes:
        RACECAR, RADAR
        Example Non-palindromes:
        TEST, ABC. HELLO
        '''
        # Method 1

        s = ""
        p = self.head

        while p:
            s += p.data
            p = p.next
        return s == s[::-1]


llist = LinkedList()
llist.append('R')
llist.append('A')
llist.append('D')
llist.append('A')
llist.append('R')
llist.print_list()
print('\n')
print(llist.is_pailndrome_1())
