class TreeNode:

	# constructor
	def __init__(self):
		self.val = 0		# an int or float
		self.leftChild = None
		self.rightChild = None

	def getLeftChild(self):
		return self.leftChild

	def setLeftChild(self, leftChild):
		self.leftChild = leftChild

	def getRightChild(self):
		return self.rightChild

	def setRightChild(self, rightChild):
		self.rightChild = rightChild

	def getVal(self):
		return self.val

	def setVal(self, val):
		self.val = val