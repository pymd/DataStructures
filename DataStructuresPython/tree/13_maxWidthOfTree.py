from TreeNode import TreeNode as Node

class Tree:

	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def _height (self, current):
		if current is None:
			return 0
		return (max(self._height(current.getLeftChild()), 
			self._height(current.getRightChild())) + 1)

	def maxWidthOfTree (self, current):
		"""
			Max width:    No. of nodes at the level which has the largest number of nodes
			Uses preOrderTraversal
			Time Complexity: O(n)
			Space: O(logn)

			IMP : Also practice, 2 other methods using Level Order Traversal
			LINK: http://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/
		"""
		count = [0] * self._height(current)		# count of nodes at EACH LEVEL of tree
		level = 0
		self._maxWidthOfTree (current, level, count)
		return max(count)

	def _maxWidthOfTree (self, current, level, count):
		if current is None:
			return
		count[level] += 1
		self._maxWidthOfTree(current.getLeftChild(), level+1, count)
		self._maxWidthOfTree(current.getRightChild(), level+1, count)

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
	#t.getRoot().getRightChild().setLeftChild(t.createNode(60))
	t.getRoot().getRightChild().setRightChild(t.createNode(70))

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print 'Max Width of the Tree is:', t.maxWidthOfTree(t.getRoot())

