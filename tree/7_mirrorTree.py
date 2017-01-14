from TreeNode import TreeNode as Node

class Tree:

	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def _swapChildren (self, current):
		temp = current.getLeftChild()
		current.setLeftChild (current.getRightChild())
		current.setRightChild (temp)

	def convertTreeToMirror (self, current):
		"""
			Convert the tree to its mirror tree.
			Starting at the bottom of the tree, go to each node, swap the left child with right child.
			Traversal: PostOrder --> First go to the LST and RST. Then process the node (swap children).
			Time Complexity: O(n)
		"""
		if current is None:
			return
		self.convertTreeToMirror(current.getLeftChild())
		self.convertTreeToMirror(current.getRightChild())
		self._swapChildren (current)

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
	t.getRoot().getRightChild().setLeftChild(t.createNode(60))
	t.getRoot().getRightChild().setRightChild(t.createNode(70))

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print "Converting the tree to mirror tree."
	t.convertTreeToMirror(t.getRoot())

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

