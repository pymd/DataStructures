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
		node.setNext(None)
		return node

	def addNode (self, val):
		node = self.createNode(val)
		node.setNext(self.head)
		self.head = node
		return node

	def printList (self):
		cur = self.head
		while cur is not None:
			print cur.getVal(),'->',
			cur = cur.getNext()
		print 'NULL'

	def middleOfList(self):
		"""
			Uses 2 scans
		"""
		cur = self.head
		length = 0
		while cur is not None:
			length += 1
			cur = cur.getNext()
		mid = length/2
		cur = self.head
		for i in range(0,mid):
			cur = cur.getNext()
		return cur

	def middleOfListSingleScan(self):
		"""
			Uses a single scan of the list.
			Uses two pointers: slow and fast.
		"""
		slow = self.head
		fast = self.head
		while (fast is not None) and (fast.getNext() is not None):
			slow = slow.getNext()
			fast = fast.getNext().getNext()
		return slow

if __name__ == '__main__':
	l = List()

	l.addNode(10)
	l.addNode(20)
	l.addNode(30)
	l.addNode(40)
	l.addNode(50)
	l.addNode(60)
	l.addNode(70)
	l.printList()
	print 'Middle of list is:', l.middleOfList()
	print 'Middle of list is:', l.middleOfListSingleScan()