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
