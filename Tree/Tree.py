class Tree:
	"""Abstract base class representing a tree structure"""

	'''~~~~~~~~~~~~~ Nested position class ~~~~~~~~~~~~~~'''

	class Position:
		"""An abstraction representing location of a single element"""
		def element(self):
			"""Return the element stored at this position"""
			raise NotImplementedError('must be implemented by a subclass')

		def __eq__(self, other):
			"""Return True if the other position represents the same location"""
			raise NotImplementedError('must be implemented by a subclass')

		def __ne__(self, other):
			"""Return True if other doesnot represent the same location"""
			return not(self == other)

	
	'''~~~~~~~~~~~~~ abstract methods of Tree ADT ~~~~~~~~~~~~~~'''
	def root(self):
		'''Return Position representing the tree's root '''

		raise NotImplementedError('must be implemented by a subclass')

	def parent(self, p):
		'''Return position p's parent (None if p is root)'''
		raise NotImplementedError('must be implemented by a subclass')

	def num_children(self, p):
		'''Return the number of children that position p has'''
		raise NotImplementedError('must be implemented by a subclass')

	def children(self, p):
		'''Generate an iteration of Positions representing p's children'''
		raise NotImplementedError('must be implemented by a subclass')	

	def is_root(self, p):
		'''Return True if position p represents the root of the Tree'''
		return self.root() == p
	
	def is_leaf(self, p):
		'''Return True if position p has no children'''
		return self.num_children(p) == 0

	def is_empty(self):
		'''Return True if tree is empty'''
		return len(self) == 0

	def depth(self, p):
		'''Return the number of levels seperating position p from the root'''
		if self.is_root(p):
			return 0
		else:
			return 1 + self.depth(self.parent(p))

	def height(self, p):
		'''Return the height of the subtree rooted at postion p'''
		if self.is_leaf(p):
			return 0
		else:
			return 1 + (max(self.height(c)) for c in self.children(p))
