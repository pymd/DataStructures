from TreeNode import TreeNode as Node

class Sums:
	def __init__(self):
		val = 0

class Tree:
	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def checkIfSumTree (self, current):
		"""
			SumTree => (Sum of Nodes in LST + Sum of Nodes in RST) for all nodes
			Time Complexity: 	O(n)

			Algorithm:	'checkIfSumTree' returns ('sumOfAllNodesRootedAtCurrent', isSumTreeOrNot)

		"""
		if current is None:
			return 0, True
		elif (current.getLeftChild() is None) and (current.getRightChild() is None):
			return current.getVal(), True
		else:
			lstSum, isLstSumTree = self.checkIfSumTree (current.getLeftChild())
			rstSum, isRstSumTree = self.checkIfSumTree (current.getRightChild())
			
			if not (isLstSumTree and isRstSumTree):
				return -1, False
			
			if current.getVal() == (lstSum + rstSum):
				return (current.getVal() + lstSum + rstSum), True
			else:
				return -1, False

	def checkIfSumTreeWithOnlyOneReturnValue (self, current, currentSum):
		"""
			SumTree => (Sum of Nodes in LST + Sum of Nodes in RST) for all nodes
			Time Complexity: 	O(n)

			Algorithm:	Without using multiple return values (so that can be implemented as is in Java)
		"""
		if current is None:
			currentSum.val = 0
			return True
		elif (current.getLeftChild() is None) and (current.getRightChild() is None):
			currentSum.val = current.getVal()
			return True
		else:
			lstSum = Sums()
			isLstSumTree = self.checkIfSumTreeWithOnlyOneReturnValue (current.getLeftChild(), lstSum)
			rstSum = Sums()
			isRstSumTree = self.checkIfSumTreeWithOnlyOneReturnValue (current.getRightChild(), rstSum)
			
			if not (isLstSumTree and isRstSumTree):
				currentSum.val = -1
				return False
			
			if current.getVal() == (lstSum.val + rstSum.val):
				currentSum.val = current.getVal() + lstSum.val + rstSum.val
				return True
			else:
				currentSum.val = -1
				return False


	def preOrderTraversal(self, current):
		if current is None:
			return
		print current.getVal(),' ',
		self.preOrderTraversal(current.getLeftChild())
		self.preOrderTraversal(current.getRightChild())

	def getRoot(self):
		return self.root

	def setRoot(self, root):
		self.root = root

if __name__ == '__main__':
	t = Tree()
	t.setRoot(t.createNode(26));
	t.getRoot().setLeftChild(t.createNode(10))
	t.getRoot().setRightChild(t.createNode(3))
	t.getRoot().getLeftChild().setLeftChild(t.createNode(4))
	t.getRoot().getLeftChild().setRightChild(t.createNode(6))
	t.getRoot().getRightChild().setRightChild(t.createNode(3))
	
	
	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print 'Is is a sumTree:', t.checkIfSumTree (t.getRoot())

	treeSum = Sums()
	print 'Is is a sumTree:', t.checkIfSumTreeWithOnlyOneReturnValue (t.getRoot(), treeSum)
	print 'Sum:',treeSum.val
	