class Solution(object):
	def isValid(self,s):
		'''
		:type s: str
		:rtype: boolean
		'''

		# stack to keep track of opening brackets
		stack = []

		# Hash map for keeping track of mappings.
		# This keeps the code very clean.
		# Also makes adding more types of paranthesis easier
		mapping = {")":"(",
					"}":"{",
					"]":"["}

		# for every bracket in the expression.
		for char in s:
			# if chat is in closing bracket
			if char in mapping:
				# if so and its non empty, pop the topmost element from the stack
				# else assign a dummy value of '#' to the top_element variable
				top_element = stack.pop() if stack else '#'

				# the mapping for the opening bracket in our hash and the top
				# element of stack dont match, return false
				if mapping[char] != top_element:
					return false
			else:
				stack.append(char)
		# in the end, if the stack is empty, then we have a valid expression
		return not stack;