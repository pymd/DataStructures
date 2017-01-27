from TreeNode import TreeNode as Node

class Tree:
	def __init__(self):
		self.root = None

	def createNode (self, val):
		node = Node()
		node.setVal(val)
		return node

	def printPaths (self, current):
		paths = []
		self.printAllRootToLeafPaths (current, paths, 0)

	def _printArray (self, paths, pathlen):
		print 'One of the paths is:',
		for i in range(pathlen):
			print paths[i]," ",
		print ''

	def printAllRootToLeafPaths (self, current, paths, pathlen):
		"""
			Print out all of its root-to-leaf paths one per line.
			Using an external queue/array of length = Max Depth of tree.
			Time Complexity: O(n)
			Space Complexity: O(logn)
		"""
		if current is None:
			return
		
		paths.append(current.getVal())
		pathlen += 1

		if (current.getLeftChild() is None) and (current.getRightChild() is None):
			# This is a leaf
			self._printArray(paths, pathlen)
		else:
			# Recurse on LST and RST
			self.printAllRootToLeafPaths(current.getLeftChild(), paths, pathlen)
			self.printAllRootToLeafPaths(current.getRightChild(), paths, pathlen)
		paths.pop()

	def preOrderTraversal(self, current):
		if current is None:
			return
		print current.getVal()," ",
		self.preOrderTraversal (current.getLeftChild())
		self.preOrderTraversal (current.getRightChild())

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
	t.getRoot().getLeftChild().getRightChild().setRightChild(t.createNode(100))
	t.getRoot().getRightChild().setLeftChild(t.createNode(60))
	t.getRoot().getRightChild().setRightChild(t.createNode(70))

	print "Doing pre-order traversal:"
	t.preOrderTraversal(t.getRoot())
	print ''

	print 'Printing all Root To Leaves Paths:'
	t.printPaths(t.getRoot())
	print ''
