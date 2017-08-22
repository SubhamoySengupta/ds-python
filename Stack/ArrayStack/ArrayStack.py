'''
	LIFO Stack ADT Implementation using python built in list 
	Methods for a stack S are:
	1. S.push(e)    -- insert new element e at the top of the stack
	2. S.pop()      -- remove and return the top most element of the stack
	3. S.top()      -- return the top most element of the stack
	4. S.is_empty() -- check if the stack is empty, returns true if empty
	5. len(S)       -- return the length of the stack
'''

class ArrayStack:
	'''
		LIFO Stack Implementation using python built in list 
	'''
	def __init__(self):
		'''Create an empty stack'''
		self._data = []

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		'''Return true if stack is empty'''
		return len(self._data) == 0

	def push(self, e):
		'''Add an element e to the top of the stack'''
		self._data.append(e)

	def top(self):
		'''
			Return the element aat the top of the stack

			Raise an exception if stack is empty
		'''
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]

	def pop(self):
		'''
			Remove and return the element from the top of the stack

			Raise an exception if the stack is empty
		'''
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data.pop()

