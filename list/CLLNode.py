class CLLNode:
	def __init__(self):
		self.val = 0
		self.next = self

	def getVal(self):
		return self.val

	def setVal(self, val):
		self.val = val

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next