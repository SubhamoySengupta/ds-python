'''
	FIFO Queue ADT implementation using singly linked list for storage
	Methods for a queue Q are:
	1. Q.enqueue(e) -- Add element e at the back of Q
	2. Q.dequeue()  -- Remove and return the final element from Q
	3. Q.is_empty() -- Check if the queue Q is empty
	4. Q.first()    -- Return the first element of Q
	4. len(Q)       -- Return the length of Q 
'''

class LinkedQueue:
	'''
		FIFO queue implementation using linked list for storage
	'''
	
	class _Node:
		""" Lightweight, non-public class for storing singly linked nodes"""

		__slots__ = '_element', '_next'
		def __init__(self, element, next):
			self._element = element
			self._next = next

	"""~~~~~~~~~~~~~~~~~~~ Stack Methods ~~~~~~~~~~~~~~~~~~~"""
	def __init__(self):
		"""Create an empty queue"""
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		"""Return the number of elements in queue"""
		return self._size

	def is_empty(self):
		"""Return True if queue is empty"""
		return self._size == 0

	def first(self):
		""" Return(but do not remove) the element at the front of the queue"""
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._head._element
	
	def dequeue(self):
		""" Return and delete the element at the front of the queue"""
		if self.is_empty():
			raise Empty('Queue is empty')
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		if self.is_empty():
			self._tail = None
		return answer

	def enqueue(self, e):
		"""Add an element to the back of the queue"""
		newest = self._Node(e, None)
		if self.is_empty():
			self._head = newest
		else:
			self._tail._next = newest
		self._tail = newest
		self._size += 1
