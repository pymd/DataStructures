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

	def getNthNodeFromEndUsingTwoScans(self, n):
		"""
			This solution assumes that 'length' of the list is not maintained.
			Thus, it uses one scan to find length of the list. And second scan,
			to find (length-n)th node from starting.
		"""
		if (n == 0) or (n > self.length):
			return None
		cur = self.head
		length = 0
		while cur != None:
			cur = cur.getNext()
			length += 1
		cur = self.head
		m = length-n
		i = 0
		while i < m and cur != None:
			cur = cur.getNext()
			i += 1
		return cur

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

	def getNthNodeFromEndRecursive(self, current, n):
		global counter
		if current is not None:
			return_value = self.getNthNodeFromEndRecursive(current.getNext(), n)
			if return_value:
				return return_value
			counter += 1
			if counter == n:
				return current
		return None

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
	node2 = l.getNthNodeFromEndUsingTwoScans(n)
	counter = 0
	node3 = l.getNthNodeFromEndRecursive(l.getHead(), n)
	if node is None:
		print n,'th node from the end is: None'
	else:
		print n,'th node from the end is:',node.getVal()

	if node2 is None:
		print n,'th node from the end is: None'
	else:
		print n,'th node from the end is:',node2.getVal()

	if node3 is None:
		print n,'th node from the end is: None'
	else:
		print n,'th node from the end is:',node3.getVal()