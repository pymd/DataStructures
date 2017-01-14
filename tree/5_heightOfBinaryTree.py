from TreeNode import TreeNode as Node

class Tree:

	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def preOrderTraversal(self, root):
		if root is None:
			return
		print root.getVal(),' ',
		self.preOrderTraversal(root.getLeftChild())
		self.preOrderTraversal(root.getRightChild())

	def heightOfTree(self, root):
		"""
			Height of tree:		{ 1  +  Maximum of (Height of LST, Height of RST) }
			Time Complexity:	O(n)	(Each node visited once)
		"""
		if root is None:
			return 0
		if (root.getLeftChild() is None) and (root.getRightChild() is None):
			# This is a leaf node
			return 1
		return 1 + max( 
			self.heightOfTree(root.getLeftChild()), 
			self.heightOfTree(root.getRightChild())
		)

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

	print "PreOrder traversal is:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print "Height of the tree is:",t.heightOfTree(t.getRoot())