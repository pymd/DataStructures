from TreeNode import TreeNode as Node

class Tree:
	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def checkChildrenSumProp(self, current):
		if (current is None) or ((current.getLeftChild() is None) and (current.getRightChild() is None)):
			return True
		
		sum = 0
		if current.getLeftChild() is not None:
			sum += current.getLeftChild().getVal()
		if current.getRightChild() is not None:
			sum += current.getRightChild().getVal()

		if sum != current.getVal():
			return False
		return True
		
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

	print 'Satisfies children sum property:', t.checkChildrenSumProp(t.getRoot())

	t2 = Tree()
	t2.setRoot(t2.createNode(100));
	t2.getRoot().setLeftChild(t2.createNode(80))
	t2.getRoot().setRightChild(t2.createNode(20))
	t2.getRoot().getLeftChild().setLeftChild(t2.createNode(50))
	t2.getRoot().getLeftChild().setRightChild(t2.createNode(30))
	t2.getRoot().getRightChild().setLeftChild(t2.createNode(15))
	t2.getRoot().getRightChild().setRightChild(t2.createNode(5))
	t2.getRoot().getRightChild().getRightChild().setLeftChild(t2.createNode(5))

	print "Doing pre-order traversal:"
	t2.preOrderTraversal(t2.getRoot())
	print ''

	print 'Satisfies children sum property:', t2.checkChildrenSumProp(t2.getRoot())