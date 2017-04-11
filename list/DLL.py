from DLLNode import Node

class DLL (object):
	"""A class representing Doubly Linked List"""
	
	def __init__(self):
		super(DLL , self).__init__()
		self.head = None

	def getHead(self):
		return self.head

	def setHead(self, head):
		self.head = head

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		node.setPrev(None)
		node.setNext(None)
		return node

	def addNode(self, val):
		node = self.createNode(val)
		node.setNext(self.head)
		if self.head is not None:
			self.head.setPrev(node)
		self.head = node

	def printList (self):
		cur = self.head
		while cur is not None:
			print cur.getVal(),'<-->',
			cur = cur.getNext()
		print 'NULL'

	def printListFromEnd (self):
		cur = self.head
		if cur is None:
			print 'NULL'
			return
		while cur.getNext() is not None:
			cur = cur.getNext()
		tail = cur
		print 'NULL',
		while cur is not None:
			print '<-->',cur.getVal(),
			cur = cur.getPrev()
		print '<--> NULL'

if __name__ == '__main__':
	l = DLL()
	l.addNode(10)
	l.addNode(5)
	l.addNode(4)
	l.addNode(3)
	l.addNode(2)
	l.addNode(1)

	l.printList()
	l.printListFromEnd()