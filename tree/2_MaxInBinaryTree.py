from TreeNode import TreeNode as Node


class Tree:
	def __init__(self):
		self.root =  None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def maxInBinaryTree (self, root):
		"""
			Visit each element of the tree recursively, and maintain a maximum.
			Recursive visit:
				Get max from LeftSubTree.
				Get max from RightSubTree.
				Compare lstMax, rstMax and root.
				Return Max.
			Time Complexity: O(n)
		"""
		if root == None:
			return -1
		lstMax = self.maxInBinaryTree (root.getLeftChild())			# Maximum val from LeftSubTree
		rstMax = self.maxInBinaryTree (root.getRightChild())		# Maximum val from RightSubTree
		maxVal = max(root.getVal(), lstMax, rstMax)					# Max of lstMax, rstMax, and root
		return maxVal

	def preOrderTraversal (self, current):
		if current == None:
			return
		self.preOrderTraversal(current.getLeftChild())
		print current.getVal()," ",
		self.preOrderTraversal(current.getRightChild())

	def getRoot(self):
		return self.root

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

	print 'Maximum element in the tree is:', tree.maxInBinaryTree (tree.getRoot())