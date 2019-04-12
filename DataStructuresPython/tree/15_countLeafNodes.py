from TreeNode import TreeNode as Node

class Tree:

	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def countLeafNodes (self, current):
		"""
			Return the total number of leaves in the Tree
			Time Complexity: O(n)
		"""
		if current is None:
			return 0
		if current.getLeftChild() is None and current.getRightChild() is None:
			return 1
		leavesInLST = self.countLeafNodes(current.getLeftChild())
		leavesInRST = self.countLeafNodes(current.getRightChild())
		return (leavesInLST + leavesInRST)

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
	t.getRoot().getRightChild().setLeftChild(t.createNode(60))
	t.getRoot().getRightChild().setRightChild(t.createNode(70))

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print "Number of leaves in the tree:",t.countLeafNodes(t.getRoot())