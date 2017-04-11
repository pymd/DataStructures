from listNode import Node

class List(object):
	"""A class representing linked list"""
	
	def __init__(self):
		super(List, self).__init__()
		self.head = None

	def getHead(self):
		return self.head

	def setHead(self, head):
		self.head = head

	def printList(self):
		cur = self.head
		while cur is not None:
			print cur.getVal(),'->',
			cur = cur.getNext()
		print 'NULL'

	def createNode(self, val):
		node = Node()
		node.setVal(val)
		return node

	def addNode(self, val):
		node = self.createNode(val)
		node.setNext(self.head)
		self.head = node

	def reverse (self):
		cur = self.head
		next = cur.getNext()
		cur.setNext(None)
		while next is not None:
			temp = next.getNext()
			next.setNext(cur)
			cur = next
			next = temp
		self.head = cur

	def deleteNodesWithGreaterNodesOnRight (self):
		self.reverse()
		cur = self.head
		while (cur is not None) and (cur.getNext() is not None):
			if (cur.getVal() > cur.getNext().getVal()):
				cur.setNext(cur.getNext().getNext())
			else:
				cur = cur.getNext()
		self.reverse()

if __name__ == '__main__':
	l = List()
	l.addNode(10)
	l.addNode(5)
	l.addNode(4)
	l.addNode(15)
	l.addNode(3)
	l.addNode(2)
	l.addNode(1)
	l.addNode(20)

	l.printList()
	l.deleteNodesWithGreaterNodesOnRight()
	l.printList()