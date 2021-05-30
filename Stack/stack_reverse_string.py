'''reverses string using a stack
'''
from stack import Stack

def reverse_string(stack,input_str):
	#Loop through the string and push contents 
	#character by character onto the stack
	for char in input_str:
		stack.push(char)

	reverse_string = ''
	
	while not stack.is_empty():
		reverse_string += stack.pop()
	return reverse_string

stack = Stack()
input_str = "Hello"
print(reverse_string(stack,input_str))	