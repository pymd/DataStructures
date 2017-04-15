from DLLNode import Node

class DLL (object):
	"""A class representing Doubly Linked List"""
	
	def __init__(self):
		super(DLL , self).__init__()
		self.head = None
		self.length = 0

	def getLength(self):
		return self.length

	def setLength(self, length):
		self.length = length

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
		"""
			Add a node to the beginning of the DLL
			O(1)
		"""
		node = self.createNode(val)
		node.setNext(self.head)
		if self.head is not None:
			self.head.setPrev(node)
		self.head = node
		self.length += 1

	def insert(self, val, position):
		"""
			Add a node at a given position in the linked list
			O(n)
		"""
		node = self.createNode(val)
		cur = self.head
		if self.head is None:
			self.head = node
			node.setNext(None)
			node.setPrev(None)
			self.length += 1
			return
		if position < 0:
			position = 0
		elif position > self.length:
			position = self.length
		if position == 0:
			cur.setPrev(node)
			node.setNext(cur)
			self.head = node
			self.length += 1
			return
		# Now 0 < pos <= length
		i = 0
		while (cur is not None) and (i < position-1):
			cur = cur.getNext()
			i += 1
		# Insert at this position
		node.setNext(cur.getNext())
		if cur.getNext() != None:			# not the last node
			cur.getNext().setPrev(node)
		cur.setNext(node)
		node.setPrev(cur)
		self.length += 1

	def insertTail(self, val):
		"""
			Add a node at the tail of the list
			O(n)
		"""
		node = self.createNode(val)
		cur = self.head
		if cur is None:
			self.head = node
			node.setNext(None)
			node.setPrev(None)
			self.length += 1
			return
		while cur.getNext() is not None:
			cur = cur.getNext()
		cur.setNext(node)
		node.setPrev(cur)
		node.setNext(None)
		self.length += 1
		return

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

	def getPosition (self, data):
		cur = self.head
		if cur is None:
			return -1
		pos = 0
		while cur is not None:
			if cur.getVal() == data:
				return pos
			pos += 1
			cur = cur.getNext()
		return -1

	def removeHead(self):
		"""
			Remove the head of the list
			O(1)
		"""
		cur = self.head
		if cur is None:
			return
		self.head = cur.getNext()
		if self.head is not None:
			(self.head).setPrev(None)
		self.length -= 1
		del cur

	def removeTail(self):
		"""
			Remove the last element of the list
			O(n)
		"""
		cur = self.head
		if cur is None:
			return
		if cur.getNext() is None:
			# Only 1 elemnet present
			self.head = None
			self.length -= 1
			del cur
			return
		while cur.getNext().getNext() is not None:
			cur = cur.getNext()
		temp = cur.getNext()
		cur.setNext(None)
		del temp

	def remove (self, position):
		"""
			Remove a node from a particular position.
		"""
		pass

	def removeMatched (self, val):
		"""
			Remove a node matching a given value.
		"""
		cur = self.head
		if cur is None:
			return
		if cur.getVal() == val:
			self.head = self.head.getNext()
			if self.head is not None:
				self.head.setPrev(None)
			self.length -= 1
			del cur
			return

		# Doubly linked list => traverse upto the required node
		while cur != None:
			if cur.getVal() == val:
				cur.getPrev().setNext(cur.getNext())
				if cur.getNext() is not None:
					cur.getNext().setPrev(cur.getPrev())
			cur = cur.getNext()
		return

	def __str__(self):
		"""
			A method to show string representation of the list
		"""
		result = '['
		if self.length == 0:
			result += ']'
			return result
		cur = self.head
		while cur is not None:
			result += str(cur.getVal())
			result += ','
			cur = cur.getNext()
		result += ']'
		return result

	def clearList(self):
		self.head = None
		self.length = 0

if __name__ == '__main__':
	l = DLL()
	l.addNode(10)
	l.addNode(5)
	l.removeHead()
	l.printList()
	l.addNode(4)
	l.addNode(3)
	l.addNode(2)
	l.addNode(1)

	l.printList()
	l.printListFromEnd()
	print 'Length of list:',l.getLength()

	ele = input('Enter the elment whose position is to be found:')
	pos = l.getPosition(ele)
	if pos == -1:
		print 'Element is not presen in the list'
	else:
		print 'Element',ele,'is present in the list at position:',pos

	l.insert(6,1)
	l.printList()
	#l.printListFromEnd()

	l.insertTail(11)
	l.printList()
	#l.printListFromEnd()

	l.removeHead()
	l.printList()
	#l.printListFromEnd()

	l.removeTail()
	l.printList()
	#l.printListFromEnd()

	print 'Deleting the element:',ele
	l.removeMatched(ele)
	l.printList()

	print l