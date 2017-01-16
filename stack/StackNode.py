class StackNode:
	"""
		A class representing a single node of a stack
	"""

	def __init__(self):
		self.val = 0
		self.next = None

	def getVal(self):
		return self.val

	def setVal(self, val):
		self.val = val

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next