from listNode import Node

class List:
	def __init__(self):
		self.head = None
		self.length = 0

	def getHead(self):
		return self.head

	def setHead(self, head):
		self.head = head

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def addNode(self, val):
		node = self.createNode(val)
		node.setNext(self.head)
		self.head = node
		self.length += 1

	def printList(self):
		current = self.head
		while current is not None:
			print current.getVal(),'->',
			current = current.getNext()
		print 'NULL'

	def getNthNodeFromEnd(self, n):
		first = self.head
		second = self.head
		i = 0
		if (n == 0) or (n > (self.length)):
			return None
		while i < n:
			second = second.getNext()
			i+=1
		# Now, first and second are (n-1) distance apart
		while second is not None:
			first = first.getNext()
			second = second.getNext()
		return first

if __name__ == '__main__':
	l = List()
	l.addNode(10)
	l.addNode(5)
	l.addNode(4)
	l.addNode(3)
	l.addNode(2)
	l.addNode(1)
	
	l.printList()

	n = input('Enter n:')
	node = l.getNthNodeFromEnd(n)
	if node is None:
		print n,'th node from the end is: None'
	else:
		print n,'th node from the end is:',node.getVal()

