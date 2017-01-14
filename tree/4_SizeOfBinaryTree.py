from TreeNode import TreeNode as Node

class Tree:
	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def preOrderTraversal(self, root):
		if root == None:
			return
		print root.getVal()," ",
		self.preOrderTraversal(root.getLeftChild())
		self.preOrderTraversal(root.getRightChild())

	def sizeOfTree(self, root):
		if root == None:
			return 0
		return (self.sizeOfTree(root.getLeftChild()) + 
			self.sizeOfTree(root.getRightChild()) + 
			1)

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

	print "Size Of the tree is:",t.sizeOfTree(t.getRoot())