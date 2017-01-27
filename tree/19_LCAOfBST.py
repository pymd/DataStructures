from TreeNode import TreeNode as Node

class Tree:

	def __init__ (self):
		self.root = None

	def createNode (self, val):
		node = Node()
		node.setVal(val)
		return node

	def lca (self, current, first, second):
		"""
			Since, this is a BST, key comparison was possible.
			See next question for LCA in Binary Tree.
			Time Complexity: 	O(log n)

			TODO: Try iterative solution later.
		"""
		if current is None:
			return None
		smaller = min(first,second)
		larger = max(first,second)
		if (smaller <= current.getVal()) and (larger >= current.getVal()):
			return current
		elif current.getVal() < smaller:
			return self.lca (current.getRightChild(), first, second)
		elif current.getVal() > larger:
			return self.lca (current.getLeftChild(), first, second)

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
	
	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print 'Lowest Common Ancestor of 10 and 14  is:', t.lca(t.getRoot(), 10, 14).getVal()
	print 'Lowest Common Ancestor of 4 and 10  is:', t.lca(t.getRoot(), 4, 10).getVal()
	print 'Lowest Common Ancestor of 14 and 22  is:', t.lca(t.getRoot(), 14, 22).getVal()
	print 'Lowest Common Ancestor of 10 and 12  is:', t.lca(t.getRoot(), 10, 12).getVal()
