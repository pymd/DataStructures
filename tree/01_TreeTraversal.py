from TreeNode import TreeNode as Node

class Stack:
	"""
		An small implementation of stack using 'list' as storage
	"""

	def __init__(self):
		self.storage = list()
		self.setTop()

	def push (self, val):
		self.storage.append (val)
		self.setTop()

	def pop (self):
		val = self.storage.pop()
		self.setTop()
		return val

	def isEmpty (self):
		if len(self.storage) == 0:
			return True
		return False

	def getTop (self):
		return self.storage[self.top]

	def setTop (self):
		if len(self.storage) == 0:
			self.top = 0
		else:
			self.top = len(self.storage) - 1

class Tree:
	"""
		Class containing iterative methods for 
			PreOrder, 
			InOrder, and 
			PostOrder
		traversal of a Binary Tree.
		Involves Stack and Backtracking. Using 'Python List' as 'Stack'.
	"""
	def __init__(self):
		self.root = None

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def iterativePreOrderTraveral (self, current):
		# TODO: Not clearly understood; do again
		stack = Stack()
		stack.push (current)
		
		while not (stack.isEmpty()):
			
			while current != None:
				print current.getVal(), " ",
				current = current.getLeftChild()
				if current != None:
					stack.push(current)

			if stack.isEmpty():
				break
			# Backtrack
			current = stack.pop()
			while (current.getRightChild() == None) and (not stack.isEmpty()):
				current = stack.pop()
			if stack.isEmpty() and current.getRightChild() == None:
				break
			stack.push(current.getRightChild())
			current = stack.getTop()

	
	def iterativeInOrderTraveral (self, current):
		# TODO: Not clearly understood; do again
		stack = Stack()
		stack.push(current)

		while not (stack.isEmpty()):
			# Go to LST
			while current != None:
				current = current.getLeftChild()
				if current != None:
					stack.push(current)
			
			# Process Root
			if stack.isEmpty():
				break
			
			# Process Root and BackTrack
			current = stack.pop()
			print current.getVal(), " ",
			while (current.getRightChild() == None) and (not stack.isEmpty()):
				current = stack.pop()
				print current.getVal(), " ",

			if stack.isEmpty() and current.getRightChild() == None:
				break
			stack.push(current.getRightChild())
			current = stack.getTop()
	
	
	def iterativePostOrderTraveral (self, current):
		# TODO: NOT IMPLEMENTED YET
		pass

	def getRoot(self):
		return self.root

	def setRoot(self, root):
		self.root = root

if __name__ == '__main__':
	tree = Tree()
	tree.setRoot(tree.createNode(10))
	tree.getRoot().setLeftChild(tree.createNode(20))
	tree.getRoot().setRightChild(tree.createNode(30))
	tree.getRoot().getLeftChild().setLeftChild(tree.createNode(40))
	tree.getRoot().getLeftChild().setRightChild(tree.createNode(50))
	tree.getRoot().getRightChild().setLeftChild(tree.createNode(60))
	tree.getRoot().getRightChild().setRightChild(tree.createNode(70))


	print 'PreOrder Traversal is:'
	tree.iterativePreOrderTraveral(tree.getRoot())
	print ''

	print 'InOrder Traversal is:'
	tree.iterativeInOrderTraveral(tree.getRoot())
	print ''

	print 'PostOrder Traversal is:'
	tree.iterativePostOrderTraveral(tree.getRoot())
	print ''