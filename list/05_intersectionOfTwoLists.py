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

	def length(self):
		cur = self.head
		l = 0
		while cur is not None:
			l += 1
			cur = cur.getNext()
		return l

	def addNode(self, val):
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

	def getIntersectionUsingLengths (self, l2):
		len1 = self.length()
		len2 = l2.length()
		i = 0
		cur1 = self.getHead()
		cur2 = l2.getHead()
		
		if len1 > len2:
			while i < (len1 - len2):
				cur1 = cur1.getNext()
				i += 1
		elif len1 < len2:
			while i < (len2 - len1):
				cur2 = cur2.getNext()
				i += 1
		while cur1 is not None and cur2 is not None:
			if cur1 is cur2:
				return cur1
			cur1 = cur1.getNext()
			cur2 = cur2.getNext()
		return None

if __name__ == '__main__':
	l = List()
	l.addNode(10)
	l.addNode(5)
	l.addNode(4)
	n = l.addNode(3)
	l.addNode(2)
	l.addNode(1)

	l.printList()

	l2 = List()
	l2.setHead(n)
	l2.addNode(100)
	l2.addNode(200)
	l2.addNode(300)
	l2.addNode(400)

	l2.printList()

	point = l.getIntersectionUsingLengths(l2)
	if point is not None:
		print 'The point of intersection of two lists is:', point.getVal()
	else:
		print 'The two lists dont intersect'
