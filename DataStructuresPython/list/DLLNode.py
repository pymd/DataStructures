class Node(object):
	"""Node for doubly linked list"""

	def __init__(self):
		super(Node, self).__init__()
		self.val = 0
		self.next = None
		self.prev = None

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next

	def getPrev(self):
		return self.prev

	def setPrev(self, prev):
		self.prev = prev

	def getVal(self):
		return self.val

	def setVal(self, val):
		self.val = val