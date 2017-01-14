from TreeNode import TreeNode as Node

class Tree:

	# constructor
	def __init__(self):
		self.root = None

	# create a new node
	def addNode (self, val):
		node = Node()
		node.setVal(val)
		return node

	def preOrderTraversal (self, root):
		if root == None:
			return
		print root.getVal()," ",
		self.preOrderTraversal(root.getLeftChild())
		self.preOrderTraversal(root.getRightChild())

	def inOrderTraversal (self, root):
		if root == None:
			return
		self.inOrderTraversal(root.getLeftChild())
		print root.getVal()," ",
		self.inOrderTraversal(root.getRightChild())

	def postOrderTraversal (self, root):
		if root == None:
			return
		self.postOrderTraversal(root.getLeftChild())
		self.postOrderTraversal(root.getRightChild())
		print root.getVal()," ",

	def getRoot(self):
		return self.root

	def setRoot (self, root):
		self.root = root


if __name__ == '__main__':
	t = Tree()
	t.setRoot(t.addNode(10));
	t.getRoot().setLeftChild(t.addNode(20))
	t.getRoot().setRightChild(t.addNode(30))
	t.getRoot().getLeftChild().setLeftChild(t.addNode(40))
	t.getRoot().getLeftChild().setRightChild(t.addNode(50))
	t.getRoot().getRightChild().setLeftChild(t.addNode(60))
	t.getRoot().getRightChild().setRightChild(t.addNode(70))

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print "Doing in-order traversal:"
	t.inOrderTraversal(t.getRoot())
	print ''

	print "Doing post-order traversal:"
	t.postOrderTraversal(t.getRoot())
