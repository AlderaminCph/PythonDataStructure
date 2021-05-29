'''
Use a stack data structure to convert integer to binary

Example: 242

242 / 2 = 121 -> 0
121 / 2 = 60 -> 1
60 / 2 = 30 -> 0
30 / 2 = 15 -> 0
15 / 2 = 7 -> 1
7 / 2 = 3 -> 1
3 / 2 = 1 -> 1
1 / 2 = 0 -> 1

'''

from stack import Stack

def div_by_2(decimal_number):
	s = Stack()
	while decimal_number > 0:
		remainder = decimal_number % 2 #get remainder
		s.push(remainder) #we push remainder onto the stack
		decimal_number = decimal_number // 2 #perform a duble division
	
	binary_number = ''

	while not s.is_empty():
		binary_number += str(s.pop())
	return binary_number

print(div_by_2(242))