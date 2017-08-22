from BinaryTree import BinaryTree
"""
	Binary Tree ADT implementation using linked list
	Methods of Binary Tree T are:
	1. T.add_root(e)		--
	2. T.add_left(p, e)		--
	3. T.add_right(p, e)	--
	4. T.replace(p, e)		--
	5. T.delete(p)			--
	6. T.attach(p, T1, T2)	--
"""

class LinkedBinaryTree(BinaryTree):
	"""Linked representation of binary tree structure"""
	class Node:
		__slots__ = '_element', '_parent', '_left', '_right'
		def __init__(self, element, parent=None, left=None, right=None):
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right

	class Position(BinaryTree.Position):
		"""An abstract representation of the location of e single element"""

		def __init__(self, container, node):
			"""Constructor should not be invoked by user"""
			self._container = container
			self._node = node

		def element(self):
			"""Return the element stored at this position"""
			return self._node._element

		def __eq__(self, other):
			"""Return True if other is a Position representing the same location"""
			return type(other) is type(self) and other._node is self._node

	def _validate(self, p):
		"""Return associated node if position is valid"""
		if not isinstance(p, slef.Position):
			raise TypeError('p must be proper Position type')
		if p._container is not self:
			raise ValueError('p does not belong to this container')
		if p._node._parent is p._node:
			raise ValueError('p is no longer valid')
		return p._node
	def _make_position(self, node):
		"""Return Position instance for given node (None if no node exist)"""
		return self.Position(self, node) if node is not None else None

	"""~~~~~~~~~~~~~~~~~~~~~~~ Binary Tree Constructor ~~~~~~~~~~~~~~~~~~~~~~~"""
	def __init__(self):
		"""Initialize an empty Binary Tree"""
		self._root = None
		self,_size = 0

	"""~~~~~~~~~~~~~~~~~~~~~~~ public accessors ~~~~~~~~~~~~~~~~~~~~~~~"""
	def __len__(self):
		"""Return the total number of elements in the tree"""
		return self._size

	def root(self):
		"""Return the total number of elements in the tree"""
		return self._make_position(self._root)

	def parent(self, p):
		"""Return the Position of p's parent (None if p is root)"""
		node = self._validate(p)
		return self._make_position(node._parent)

	def left(self, p):
		"""Return the Position of p's left child (None if p has no left child)"""
		node = self._validate(p)
		return self._make_position(node._right)

	def num_children(self, p):
		"""Return the number of children of Position p"""
		node = self._validate(p)
		count = 0
		if node._left is not None:
			count += 1
		if node._right is not None:
			count += 1
		return count

	def _add_root(self, e):
		"""
			Place element e at the root of an empty tree and return new Position
			Raise ValueError if tree is nonempty
		"""

		if self._root is not None:
			raise ValueError('Root already exists')
		self._size = 1
		self._root = self._Node(e)
		return self._make_position(self._root)

	def _add_left(self, p, e):
		"""
			Create a new left child for Position p, storing element _element
			Return position of new node
			Raise ValueError if Position p is invalid or p already has a left child
		"""
		node = self._validate(p)
		if node._leftt is not None:
			raise ValueError('Left child exists')
		self._size += 1
		node._left = self._Node(e, node)
		return self._make_position(node._left)

	def _add_left(self, p, e):
		"""
			Create a new right child for Position p, storing element _element
			Return position of new node
			Raise ValueError if Position p is invalid or p already has a right child
		"""
		node = self._validate(p)
		if node._right is not None:
			raise ValueError('Right child exists')
		self._size += 1
		node._right = self._Node(e, node)
		return self._make_position(node._right)

	def _replace(self, p, e):
		"""Replace the element at Position p with e, and return old element"""
		node = self._validate(p)
		old, node._element = node._element, e
		return old

	def _delete(self, p):
		"""
			Delete the node at Position p, and replace it with its child
			Return the element that had been stored at Position p
			Raise ValueError if Position p is invalid or p has the two children
		"""

		node = self._validate(p)
		if self.num_children(p) == 2:
			raise ValueError('p has two children')
		child = node._left if node._left else node._right
		if child is not None:
			child._parent = node._parent
		if node is self._root:
			self._root = child
		else:
			parent = node._parent
			if node is parent._left:
				parent._left = child
			else:
				parent._right = child
		self._size -= 1
		node._parent = node
		return node._element

	def _attach(self, p, t1, t2):
		"""Attach trees t1 and t2 as left and right subtrees of external p"""
		node = self._validate(p)
		if not self.is_leaf(p):
			raise ValueError('position p must be leaf')
		if not type(self) is type(t1) is type(t2):
			raise TypeError('Tree types must match')
		self._size += len(t1) + len(t2)
		if not t1.is_empty():
			t1._root._parent = node
			node._left = t1._root
			t1._root = None
			t1._size = 0
		if not t2.is_empty():
			t2._root._parent = node
			node._right = t2._root
			t2._root = None
			t2._size = 0