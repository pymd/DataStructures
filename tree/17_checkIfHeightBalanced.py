from TreeNode import TreeNode as Node

class Tree:
	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def height(self, current):
		"""
			Time Complexity: O(n)
		"""
		if current is None:
			return 0
		return (max(self.height(current.getLeftChild()), self.height(current.getRightChild())) + 1)

	def isBalanced (self, current):
		"""
			Balanced => 
				1. LST is Balanced
				2. RST is Balanced
				3. abs(Height of LST - Height of RST) <= 1
			
			Time Complexity: O(n^2)		: 	IMP: SOMETHING SEEMS WRONG ???	It should be O(n*logn)

			Worst Case:		Perfectly Balanced Binary Tree (For every node, height has to be checked)

			Recusion:	T(n) = 2T(n/2) + O(n)
			TODO: CHECK COMPLEXITY
		"""
		if current is None:
			return True

		if not (self.isBalanced(current.getLeftChild()) and self.isBalanced(current.getRightChild())):
			return False

		lstHeight = self.height(current.getLeftChild())			# O(n)
		rstHeight = self.height(current.getRightChild())		# O(n)
		if abs(rstHeight-lstHeight) <= 1:
			return True
		return False

	def isBalancedEfficient (self, current, distanceFromRoot):
		"""
			Time Complexity: O(n)

			Worst Case:		Perfectly Balanced Binary Tree

			IMP: For JAVA (multiple returns not allowed), create a 'class Height', and use a new 
			object for every root, LST, RST; and set the height of tree rooted at current in that object.
		"""
		if current is None:
			return True, distanceFromRoot

		isBalancedLst, maxLSTHeight = self.isBalancedEfficient(current.getLeftChild(), distanceFromRoot+1)
		isBalancedRst, maxRSTHeight = self.isBalancedEfficient(current.getRightChild(), distanceFromRoot+1)

		if isBalancedLst and isBalancedRst and abs(maxLSTHeight - maxRSTHeight) <= 1:
			return True,max(maxLSTHeight,maxRSTHeight)

		return False,max(maxLSTHeight,maxRSTHeight)


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
	t.getRoot().getLeftChild().setRightChild(t.createNode(90))
	t.getRoot().getLeftChild().getRightChild().setLeftChild(t.createNode(50))
	t.getRoot().getLeftChild().getRightChild().getLeftChild().setLeftChild(t.createNode(50))
	t.getRoot().getRightChild().setLeftChild(t.createNode(60))
	t.getRoot().getRightChild().setRightChild(t.createNode(70))
	#t.getRoot().getRightChild().getRightChild().setRightChild(t.createNode(100))
	#t.getRoot().getRightChild().getRightChild().getRightChild().setRightChild(t.createNode(100))

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print 'Is the tree height balanced? ', t.isBalanced(t.getRoot())

	print 'Is the tree height balanced? ', t.isBalancedEfficient(t.getRoot(),0)