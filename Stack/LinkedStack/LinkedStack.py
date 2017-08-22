""" 
    LIFO Stack implementation using a singly linked list for storage
    Methods for a stack S are:
        1. S.push(e)    -- insert new element e at the top of the stack
        2. S.pop()      -- remove and return the top most element of the stack
        3. S.top()      -- return the top most element of the stack
        4. S.is_empty() -- check if the stack is empty, returns true if empty
        5. len(S)       -- return the length of the stack
"""

class LinkedStack:
    """LIFO Stack implementaton using a singly list for storage"""

    """~~~~~~~~~~~~~~~~~~ nested _Node class ~~~~~~~~~~~~~~~~~~"""
    class _Node:

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    """ ~~~~~~~~~~~~~~~~~~ stack methods ~~~~~~~~~~~~~~~~~~ """
    def __init__(self):
        """ Create an empty stack """
        self._head = None
        self._size = 0

    def __len__(self):
        """ Return the number of elements in the stack """
        return self._size

    def is_empty(self):
        """ Return True if the stack is empty """
        return self._size == 0

    def push(self, e):
        """ Add element e to the top of the stack """
        self._head = self._Node(e, self._head)

    def top(self):
        """ 
            Return the element at the top of the stack 
            Raise Empty exception if the stack is empty
        """

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def pop(self):
        """ 
            Return and delete the element at the top of the stack 
            Raise Empty exception if the stack is empty
        """            

        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
