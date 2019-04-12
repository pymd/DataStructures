from listNode import Node

class List:
	def __init__(self):
		self.head = None

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

	def printList(self):
		current = self.head
		while current is not None:
			print current.getVal(),'->',
			current = current.getNext()
		print 'NULL'

	def reverse(self):
		prev = None
		current = self.head
		while current is not None:
			next = current.getNext()
			current.setNext(prev)
			prev = current
			current = next
		self.head = prev
		return

	def recursiveReverse(self, head):
		"""
			1-> 2-> 3-> 4-> 5-> NULL

	 NULL <-1 	2-> 3-> 4-> 5-> NULL

	 NULL <-1 <-2   3-> 4-> 5-> NULL

	 NULL <-1 <-2 <-3 <-4 <-5
		
		"""
		if head is None:
			return None

		# Recursive calls
		node = self.recursiveReverse(head.getNext())

		# Processing

		# Remove the current's next
		head.setNext(None)

		# Set node
		if node is None:
			self.head = head
			return head

		# Set the returned node's next to current
		node.setNext(head)

		# Return the current node
		return head

if __name__ == '__main__':
	l = List()
	l.addNode(10)
	l.addNode(5)
	l.addNode(4)
	l.addNode(3)
	l.addNode(2)
	l.addNode(1)

	l.printList()
	l.reverse()
	l.printList()
	node = l.recursiveReverse(l.getHead())
	l.printList()
