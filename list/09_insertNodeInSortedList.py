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

	def addNodeToSortedList(self, val):
		node = self.createNode(val)
		cur = self.head
		if cur is None:
			self.head = node
			return
		else:
			if cur.getVal() >= val:
				# Insert at head
				node.setNext(self.head)
				self.head = node
				return
		while cur != None:
			if cur.getVal() <= val:
				if cur.getNext() != None:
					if cur.getNext().getVal() >= val:
						break
				else:
					break
			cur = cur.getNext()
		next = cur.getNext()
		cur.setNext(node)
		node.setNext(next)

	def printList(self):
		cur = self.head
		while cur is not None:
			print cur.getVal(),'->',
			cur = cur.getNext()
		print 'NULL'

if __name__ == '__main__':
	l = List()
	l.addNodeToSortedList(20)
	l.addNodeToSortedList(10)
	l.printList()
	l.addNodeToSortedList(50)
	l.addNodeToSortedList(40)
	l.printList()
	l.addNodeToSortedList(30)

	l.printList()