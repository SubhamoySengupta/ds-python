'''
	FIFO DE Queue ADT implementation using doubly linked list
	Methods for a dequeue Q are:
	1. Q.add_first(e)   -- Add element e in front of Q
	2. Q.add_last(e)    -- Add element e at the back of Q
	3. Q.delete_first() -- Remove and return the first element from Q
	4. Q.delete_last()  -- Remove and return the last element from Q
	5. Q.is_empty()     -- Check if the dequeue Q is empty
	6. Q.first()        -- Return the first element of Q
	7. Q.last()         -- Return the last element of Q
	8. len(Q)           -- Return the length of Q
'''


""" Implementation of doubly linked list"""

class DoublyLinkedList:

	class _Node:

		__slots__ = '_element', '_prev', '_next'

		def __init__(self, element, prev, next):
			self._element = element
			self._prev = prev
			self._next = next


	def __init__(self):
		"""Initialize an empty doubly linked list"""
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0

	def __len__(self):
		"""Return length of the list"""
		return self._size

	def is_empty():
		"""Return True if stack is empty"""
		return self._size == 0

	def insert_between(self, e, predecessor, successor):
		"""Add new element between two nodes and return the new node"""
		newest = self._Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1
		return newest

	def delete_node(self, node):
		"""Delete nonsentinal node and return its element"""
		predecessor = node._prev
		successor = node._next
		predecessor._next = successor
		successor._prev = predecessor
		self._size -= 1
		element = node._element
		node._prev = node._element = node._next = None
		return element




class LinkedDeQueue(DoublyLinkedList):
	"""Implementation of DeQueue using doubly linked list"""

	def first(self):
		'''Return (but not remove) the element at front of the queue'''
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._header._next._element

	def last(self):
		'''Return (but not remove) the element at the back of dequeue'''
		if self.is_empty():
			raise Empty('Queue is empty')
		self._trailer._prev._element
	
	def insert_first(self, e):
		"""Add element at the back of DeQueue"""
		self.insert_between(e, self._header, self._header._next)

	def insert_last(self, e):
		'''Add an element at the back of dequeue'''
		self.insert_between(e, self._trailer._prev, self._trailer)

	def delete_first(self):
		if self.is_empty():
			raise Empty('DeQueue is empty')
		return self.delete_node(self._header._next)

	def delete_last(self):
		if self.is_empty():
			raise Empty('DeQueue is empty')
		return self.delete_node(self._trailer._prev)
