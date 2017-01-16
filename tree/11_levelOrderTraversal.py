from TreeNode import TreeNode as Node

class Tree:
	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def levelOrderTraveral (self, root):
		queue = list()
		queue.insert(0, root)
		while len(queue) > 0:
			self.__levelOrderTraversal (queue)

	def __levelOrderTraversal (self, queue):
		root = queue.pop()
		if root is None:
			return
		print root.getVal(), ' ',
		if root.getLeftChild() is not None:
			queue.insert(0, root.getLeftChild())
		if root.getRightChild() is not None:
			queue.insert(0, root.getRightChild())

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

	print "Doing level-order traversal:"
	t.levelOrderTraveral(t.getRoot())
	print ''
