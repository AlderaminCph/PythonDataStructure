'''
Use a stack to check whether or not a string has balanced usage of parenthesis

Example:
	(), ()(), (({[]})) <-- Balanced
	((), [][ <-- not Balanced
'''

from stack import Stack

def is_match(p1,p2):
	'''function that check if two parenthesis correspond to each other
	'''
	return p1 + p2 in ["()", "{}", "[]"]

def is_parenth_balanced(parenth_string):
	''' function that checks whether or not a string of parenthesis is balanced 
	'''
	s = Stack() #create a stack object
	is_balanced = True # a boolean flag
	index = 0

	while index < len(parenth_string) and is_balanced:
		char = parenth_string[index] #grub the string character
		if char in '({[': #check if the parenthis is an opening
			s.push(char) #push an opening parenthis onto the stack
		elif char in ')}]': #our character is a closing parenthis
			if s.is_empty(): # check if the stack is empty
				is_balanced = False # the string is not balanced
			else: # the stack is not empty
				top = s.pop()
				if not is_match(top,char):
					is_balanced = False
		index += 1

	if s.is_empty() and is_balanced:
		return True
	else:
		return False
