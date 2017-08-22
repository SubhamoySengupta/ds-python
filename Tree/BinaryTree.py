from Tree import Tree

class BinaryTree(Tree):
	"""Abstract Base Class representing a binary tree structure"""

	def left(self, p):
		"""
			Return a Position representing p's left child
			Return None if p does not have a left child
		"""
		raise NotImplementedError('must be implemented by subclass')

	def right(self, p):
		"""
			Return a Position representing p's right child
			Return None if p does not have a right child
		"""
		raise NotImplementedError('must be implemented by a subclass')

	def sibling(self, p):
		"""Return a Position representing p's sibling"""
		parent = self.parent(p)
		if parent is None:
			return None
		else:
			if p == self.left(parent):
				return self.right(parent)
			else:
				return self.left(parent)

	def children(self, p):
		if self.left(p) is not None:
			yield self.left(p)
		if self.right(p) is not None:
			yield self.right(p)
