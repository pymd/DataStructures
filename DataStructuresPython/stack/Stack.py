from StackNode import StackNode as Node

class Stack:

	class EmptyStackException (Exception):
		pass

	class FullStackException (Exception):
		pass

	def __init__(self):
		self.__top = None
		self.__size = 0

	def push (self, data):
		if self.isFull():
			raise self.FullStackException('Stack is full. Cannot push more elements onto stack. Stack size: ' + str(self.size()))
		node = Node()
		node.setVal(data)
		node.setNext(self.getTop())
		self.setTop (node)
		self.setSize(self.size() + 1)
		return

	def pop (self):
		if self.getTop() is None:
			raise self.EmptyStackException('No more elements to pop')

		nextTop = self.getTop().getNext()
		top = self.getTop()
		self.getTop().setNext(None)
		self.setTop(nextTop)
		self.setSize(self.size() - 1)
		return top

	def size (self):
		return self.__size

	def isEmpty (self):
		if self.__size is 0:
			return True
		return False

	def isFull (self):
		if self.size() >= 10:
			return True
		return False

	def top (self):
		if self.getTop() is None:
			return -1
		return self.getTop().getVal()

	def getTop (self):
		return self.__top

	def setTop (self, top):
		self.__top = top

	def setSize (self, size):
		self.__size = size

	def printStack (self):
		print 'The stack is:'
		if self.getTop() is None:
			print 'Empty'
			return
		while self.size() > 0:
			print '    ',self.pop().getVal(),'    '
		print ''
		return

if __name__ == '__main__':
	stack = Stack()
	print 'Pushing to stack: ',1
	stack.push(1)
	stack.printStack()

	print 'Pushing to stack: ',1
	stack.push(1)
	print 'Pushing to stack: ',2
	stack.push(2)
	print 'Pushing to stack: ',3
	stack.push(3)
	print 'Pushing to stack: ',4
	stack.push(4)
	stack.printStack()

	print 'Pushing to stack: ',1
	stack.push(1)
	print 'Pushing to stack: ',2
	stack.push(2)
	print 'Pushing to stack: ',3
	stack.push(3)
	print 'Size of stack: ', stack.size()
	print 'Pushing to stack: ',4
	stack.push(4)
	print 'Popping from stack'
	stack.pop()
	print 'Popping from stack'
	stack.pop()
	print 'Top of stack: ', stack.top()
	print 'Popping from stack'
	stack.pop()
	stack.printStack()
	print 'Popping from stack'
	stack.pop()
	stack.printStack()