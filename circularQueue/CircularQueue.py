""" FIFO implementation of cicularQueue using circular linked list ADT
	Methods for a queue Q are:
	1. Q.enqueue(e) -- Add element e at the back of Q
	2. Q.dequeue()  -- Remove and return the final element from Q
	3. Q.is_empty() -- Check if the queue Q is empty
	4. Q.first()    -- Return the first element of Q
	4. len(Q)       -- Return the length of Q 
	5. rotate()     -- Rotate front element to the back of queue
"""

class CircularQueue:
	"FIFO implementation of Circular Queue using circular linked list ADT"

	"""~~~~~~~~~~~~~~~~~~~~ Linked List Node class ~~~~~~~~~~~~~~~~~~~~"""
	class _Node:
		"""Lightweight, nonpublic class for storing a singly linked node."""
		__slots__ = '_element', '_next'
		def __init__(self, element, next):
			self._element = element
			self._next = next

	"""~~~~~~~~~~~~~~~~~~~~ Circular Queue Methods ~~~~~~~~~~~~~~~~~~~~"""		
	def __init__(self):
		"""Initialize an empty circular queue"""
		self._tail = None
		self._size = 0

	def __len__(self):
		"""Return length of queue"""
		return self._size

	def is_empty(self):
		"""Return True if queue is empty"""
		return self._size == 0

	def first(self):
		"""
			Return (but donot remove) the first element of the queue
			Raise an execption if queue is empty
		"""
		if self.is_empty():
			raise Empty('Queue is empty')
		head = self._tail._next
		return head._element

	def dequeue(self):
		"""
			Remove and return the first element of the queue
			Raise an execption if queue is empty
		"""
		if self.is_empty():
			raise Empty('Queue is empty')
		old_head = self._tail._next
		if self._size == 1:
			self._tail = None
		else:
			self._tail._next = old_head._next
		self._size -= 1
		return old_head._element

	def enqueue(self, e):
		""" Add an element to the back of queue"""
		newest = self._Node(e, None)
		if self.is_empty():
			newest._next = newest
		else:
			newest._next = self._tail._next
			self._tail._next = newest
		self._tail = newest
		self._size += 1

	def rotate(self):
		"""Rotate front element to the back of queue"""
		if self._size > 0:
			self._tail = self._tail._next
