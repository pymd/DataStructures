from TreeNode import TreeNode as Node

class Height:
	def __init__(self):
		self.height = 0

class Tree:
	def __init__(self):
		self.root = None

	def createNode (self, val):
		node = Node()
		node.setVal(val)
		return node

	def diameter(self, current):
		height = Height()
		diam = self.__diameter(current, height)
		print 'Height of tree is :',height.height
		print 'Diameter of tree is :',diam
		return diam

	def __diameter (self, current, heightObj):
		"""
			An example of a 'Bottom up' algorithm
			Time Complexity: 	O(n)
		"""
		if current is None:
			heightObj.height = 0
			return 0

		lstHeight = Height()
		rstHeight = Height()

		# Recursive calls
		maxDiameterLST = self.__diameter (current.getLeftChild(), lstHeight)
		maxDiameterRST = self.__diameter (current.getRightChild(), rstHeight)

		# Processing part

		# set the height
		heightObj.height = max (lstHeight.height, rstHeight.height) + 1

		# calculate the diameter
		diam = max (maxDiameterLST, maxDiameterRST, (1 + lstHeight.height + rstHeight.height))
		
		print 'For: ', current.getVal(),' ',
		print 'Height = ', heightObj.height,' ',
		print 'maxDiameterLST = ', maxDiameterLST,' ',
		print 'maxDiameterRST = ', maxDiameterRST,' ',
		print 'diam = ', diam
		
		return diam


	def preOrderTraversal (self, current):
		if current is None:
			return 
		print current.getVal(), ' ',
		self.preOrderTraversal(current.getLeftChild())
		self.preOrderTraversal(current.getRightChild())

	def getRoot(self):
		return self.root

	def setRoot(self, root):
		self.root = root

if __name__ == '__main__':
	t = Tree()
	t.setRoot(t.createNode(10));
	t.getRoot().setLeftChild(t.createNode(20))
	t.getRoot().setRightChild(t.createNode(30))
	t.getRoot().getLeftChild().setLeftChild(t.createNode(40))
	t.getRoot().getLeftChild().setRightChild(t.createNode(50))
	t.getRoot().getRightChild().setLeftChild(t.createNode(60))
	t.getRoot().getRightChild().setRightChild(t.createNode(70))

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	t.diameter(t.getRoot())

