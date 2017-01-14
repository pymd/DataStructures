from TreeNode import TreeNode as Node

class Tree:

	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def deleteTree(self, current):
		"""
			Delete a tree. Uses PostOrderTraversal to first delete the Children.
			Note: Doesn't delete the tree root. (Delete it from calling function)
			Time Complexity: O(n)
		"""
		if current is None:
			return
		self.deleteTree (current.getLeftChild())
		self.deleteTree (current.getRightChild())
		
		print 'Nodes being deleted are:',
		if current.getLeftChild() is not None:
			print current.getLeftChild().getVal(),
		if current.getRightChild() is not None:
			print current.getRightChild().getVal()
		
		current.setLeftChild (None)
		current.setRightChild (None)

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
	t.getRoot().getRightChild().getLeftChild().setRightChild(t.createNode(80))
	t.getRoot().getRightChild().getRightChild().setRightChild(t.createNode(90))

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print 'Deleting the tree'
	t.deleteTree(t.getRoot())
	print 'Tree Deleted. Tree Root (not deleted) is:',t.getRoot().getVal()

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''