'''
	FIFO Queue ADT implementation using python built in list
	Methods for a queue Q are:
	1. Q.enqueue(e) -- Add element e at the back of Q
	2. Q.dequeue()  -- Remove and return the final element from Q
	3. Q.is_empty() -- Check if the queue Q is empty
	4. Q.first()    -- Return the first element of Q
	4. len(Q)       -- Return the length of Q 
'''

class ArrayQueue:
	'''
		FIFO queue implementation using Python list
	'''
	DEFAULT_CAPACITY = 10
	def __init(self):
		'''Create an empty queue'''
		self._data = [None] + ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		'''Return the number of elements in the queue'''
		return self._size

	def is_empty(self):
		'''Return true if queue is empty'''
		return self._size == 0

	def first(self):
		'''
			Return the element in front of the queue

			Raise an exception if queue is empty
		'''
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._data[self._front]

	def dequeue(self):
		'''
			Remove and return the first element of the queue

			Raise an exception if queue is empty
		'''
		if  self.is_empty():
			raise Empty('Queue is empty')
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		self._size  -= 1
		return answer

	def enqueue(self, e):
		'''Add an element e to the back of queue'''
		if self._size == len(self._data):
			self._resize(2 * len(self._data))
			avail = (self._front + self._size) % len(self._data)
			self._data[avail] = element
			self._size += 1

	def _resize(self, cap):
		'''
			Resize to a new list capacity >= len(self)

			We assume cap >= len(self)
		'''
		old = self._data
		self._data = [None] * cap
		walk = self.front
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1 + walk) % len(old)
		self._front = 0
		
