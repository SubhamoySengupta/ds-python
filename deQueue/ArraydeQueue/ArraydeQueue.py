'''
	FIFO DE Queue ADT implementation using python built in list
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

	def add_first(self, e):
		'''Add an element e in front of dequeue'''
		if self._size == len(self._data):
			self._resize(2 * len(self._data))
			avail = (self._front + self._size) % len(self._data)
			self._data[avail] = element
			self._size += 1

	def add_last(self, e):
		'''Add an element e to the back of dequeue'''
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
		
