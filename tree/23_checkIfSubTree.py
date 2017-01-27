from TreeNode import TreeNode as Node

class Tree:

	def __init__ (self):
		self.root = None

	def createNode (self, val):
		node = Node()
		node.setVal(val)
		return node

	def _checkForIdenticalTrees (self, cur1, cur2):
		"""
			Time complexity: O(n)
		"""
		if cur1 is None and cur2 is None:
			return True
		elif cur1 is None or cur2 is None:
			return False
		return ((cur1.getVal() == cur2.getVal()) 
				and self._checkForIdenticalTrees(cur1.getLeftChild(), cur2.getLeftChild()) 
				and self._checkForIdenticalTrees(cur1.getRightChild(),cur2.getRightChild()))

	def checkSubTree(self, cur1, cur2):
		"""
			Time complexity: 	O(m*n)
			as for every node, you're checking whether subtree starts at this node
		"""

		if cur2 is None:
			return True

		if (cur1 is None) and (cur2 is not None):
			return False
		
		# For every node in cur1, check if sub tree starts at this node
		foundSubTree = self._checkForIdenticalTrees (cur1, cur2)
		if foundSubTree:
			return True
		
		foundInLst = self.checkSubTree(cur1.getLeftChild(), cur2)
		foundInRst = self.checkSubTree(cur1.getRightChild(), cur2)
		return (foundInLst or foundInRst)
		
	def preOrderTraversal (self, current):
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
	t.setRoot(t.createNode(20));
	t.getRoot().setLeftChild(t.createNode(8))
	t.getRoot().setRightChild(t.createNode(22))
	t.getRoot().getLeftChild().setLeftChild(t.createNode(4))
	t.getRoot().getLeftChild().setRightChild(t.createNode(12))
	t.getRoot().getLeftChild().getRightChild().setLeftChild(t.createNode(10))
	t.getRoot().getLeftChild().getRightChild().setRightChild(t.createNode(14))
	
	print "Doing pre-order traversal for tree 1:"
	t.preOrderTraversal(t.getRoot())
	print ''

	t2 = Tree()
	t2.setRoot(t.createNode(12))
	t2.getRoot().setLeftChild(t.createNode(10))
	t2.getRoot().setRightChild(t.createNode(14))

	print 'Is t2 subtree of t1 ?:', t.checkSubTree(t.getRoot(), t2.getRoot())
