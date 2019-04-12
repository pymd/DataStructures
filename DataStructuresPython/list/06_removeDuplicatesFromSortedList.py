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
		cur = self.head
		while cur is not None:
			print cur.getVal(),'->',
			cur = cur.getNext()
		print 'NULL'

	def removeDuplicates(self):
		if self.head is None:
			return None
		current = self.head
		next = current.getNext()
		while current is not None:
			while (next is not None) and (current.getVal() == next.getVal()):
				next = next.getNext()
			current.setNext(next)
			current = current.getNext()

if __name__ == '__main__':
	l = List()
	l.addNode(10)
	l.addNode(10)
	l.addNode(9)
	l.addNode(7)
	l.addNode(5)
	l.addNode(5)
	l.addNode(4)
	l.addNode(3)
	l.addNode(3)
	l.addNode(2)
	l.addNode(1)

	l.printList()

	l.removeDuplicates()
	l.printList()