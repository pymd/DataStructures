from TreeNode import TreeNode as Node

class Tree:
	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def levelOfNode (self, val, current):
		return self.__levelOfNode(val, 1, current)

	def __levelOfNode (self, val, level, current):
		if current is None:
			return -1
		if current.getVal() == val:
			return level
		else:
			leftTree = self.__levelOfNode(val, level+1, current.getLeftChild())
			if leftTree != -1:
				return leftTree
			else:
				rightTree = self.__levelOfNode(val, level+1, current.getRightChild())
				return rightTree

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

	print 'Level of node 40 is:', t.levelOfNode(40, t.getRoot())
	print 'Level of node 10 is:', t.levelOfNode(10, t.getRoot())
	print 'Level of node 30 is:', t.levelOfNode(30, t.getRoot())
	print 'Level of node 70 is:', t.levelOfNode(70, t.getRoot())
	print 'Level of node 90 is:', t.levelOfNode(90, t.getRoot())

