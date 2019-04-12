from TreeNode import TreeNode as Node

class Tree:
	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def preOrderTraversal(self, current):
		if current is None:
			return
		print current.getVal(),' ',
		self.preOrderTraversal(current.getLeftChild())
		self.preOrderTraversal(current.getRightChild())

	def printAncestors (self, current, val):
		"""
			Time Complexity: 	O(n)
		"""
		if current is None:
			return False
		if current.getVal() == val:
			return True
		
		foundInLst = self.printAncestors(current.getLeftChild(), val)
		foundInRst = self.printAncestors(current.getRightChild(), val)
		
		if foundInLst or foundInRst:
			print current.getVal(),' ',
			return True
		return False

	def getRoot(self):
		return self.root

	def setRoot(self, root):
		self.root = root

if __name__ == '__main__':
	t = Tree()
	t.setRoot(t.createNode(20));
	t.getRoot().setLeftChild(t.createNode(8))
	t.getRoot().setRightChild(t.createNode(22))
	t.getRoot().getLeftChild().setLeftChild(t.createNode(4))
	t.getRoot().getLeftChild().setRightChild(t.createNode(12))
	t.getRoot().getLeftChild().getRightChild().setLeftChild(t.createNode(10))
	t.getRoot().getLeftChild().getRightChild().setRightChild(t.createNode(14))
	
	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print 'Ancestor of 12 is:',
	t.printAncestors(t.getRoot(), 12)