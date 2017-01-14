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

	def searchInTree (self, root, element):
		"""
			Recursively visit each element of the tree.
			Return True if found.
			Time Complexity: O(n)
		"""
		if root == None:
			return False
		if root.getVal() == element:
			return True
		return (self.searchInTree(root.getLeftChild(), element) or 
			self.searchInTree(root.getRightChild(), element))

	# Getter for Root
	def getRoot(self):
		return self.root

	# Setter for Root
	def setRoot(self, root):
		self.root = root


if __name__ == '__main__':
	tree = Tree()
	tree.setRoot(tree.createNode(10))
	tree.getRoot().setLeftChild(tree.createNode(20))
	tree.getRoot().setRightChild(tree.createNode(30))
	tree.getRoot().getLeftChild().setLeftChild(tree.createNode(40))
	tree.getRoot().getLeftChild().setRightChild(tree.createNode(50))
	tree.getRoot().getRightChild().setLeftChild(tree.createNode(60))
	tree.getRoot().getRightChild().setRightChild(tree.createNode(70))

	print 'PreOrder Traversal is:'
	tree.preOrderTraversal(tree.getRoot())
	print ''

	element = input('Enter the element you want to search in the Tree:')
	result = tree.searchInTree (tree.getRoot(), element)
	if result:
		print 'The element',element,'exists in the tree'
	else:
		print 'The element',element,'DOES NOT exist in the tree'