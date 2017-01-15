from TreeNode import TreeNode as Node

class Tree:
	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def findPath (self, current, sumInPaths):
		"""
			Subtract each node's value from sumInPaths.
			If leaf => compare sumInPaths with leaf's node value.
			Time Complexity: O(n)
		"""
		if current is None:
			return False
		if (current.getLeftChild() is None) and (current.getRightChild() is None) and (current.getVal() == sumInPaths):
			# This is the leaf, compare the sumInPaths value to this node's value
			return True
		else:
			return (self.findPath (current.getLeftChild(), sumInPaths - current.getVal()) 
				or self.findPath(current.getRightChild(), sumInPaths - current.getVal()))

	def preOrderTraversal(self, current):
		if current is None:
			return
		print current.getVal()," ",
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
	t.getRoot().getLeftChild().getRightChild().setRightChild(t.createNode(100))
	t.getRoot().getRightChild().setLeftChild(t.createNode(60))
	t.getRoot().getRightChild().setRightChild(t.createNode(70))

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	sumInPaths = input('Enter the sum to check in tree paths:')

	print 'Path with given sum exists? :', t.findPath(t.getRoot(), sumInPaths)
