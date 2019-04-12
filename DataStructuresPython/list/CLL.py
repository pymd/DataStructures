from CLLNode import CLLNode as Node

class CLL:
	def __init__(self):
		"""
			Instead of 'head', maintaining a 'tail' pointer is more beneficial for 
			adding/deleting nodes in the list before/after head.
		"""
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
		"""
			Add node BEFORE the head of the list.
			Becomes easier if 'tail' of list is stored Instead of head.
		"""
		node = self.createNode(val)
		if self.head is None:
			self.head = node
			return
		cur = self.head.getNext()
		while cur.getNext() != self.head:
			cur = cur.getNext()
		cur.setNext(node)
		node.setNext(self.head)
		self.head = node
		return

	def removeNode(self):
		"""
			Remove a node from head of list.
			Becomes easier if 'tail' of list is stored instead of head.
		"""
		cur = self.head
		if cur is None:
			return
		if self.head.getNext() == self.head:
			self.head = None
			del cur
			return
		cur = cur.getNext()
		while cur.getNext() != self.head:
			cur = cur.getNext()
		cur.setNext(self.head.getNext())
		temp = self.head
		self.head = cur.getNext()
		del temp
		return

	def printList(self):
		cur = self.head
		if cur is None:
			print 'NULL'
			return
		print cur.getVal(),',',
		cur = cur.getNext()
		while cur != self.head:
			print cur.getVal(),',',
			cur = cur.getNext()
		print ''

	def contains(self, val):
		if self.head is None:
			return False
		cur = self.head
		if cur.getVal() == val:
			return True
		cur = cur.getNext()
		while cur != self.head:
			if cur.getVal() == val:
				return True
			cur = cur.getNext()
		return False

	def isEmpty(self):
		if self.head is None:
			return True
		return False

	def clearList(self):
		self.head = None

	def __str__(self):
		result = "["
		cur = self.head
		if cur is None:
			result += "]"
			return result
		result += str(cur.getVal())
		cur = cur.getNext()
		while cur != self.head:
			result += ', '
			result += str(cur.getVal())
			cur = cur.getNext()
		result += "]"
		return result

	def getLength(self):
		"""
			Not maintaining a length variable here.
			Thus, need to traverse the whole list.
		"""
		cur = self.head
		length = 0
		if cur is None:
			return length
		cur = cur.getNext()
		length += 1
		while cur != self.head:
			cur = cur.getNext()
			length += 1
		return length

	def remove(self, val):
		"""
			Assuming we've a 'head' pointer to the linked list
		"""
		cur = self.head
		# 0 nodes
		if cur is None:
			return None

		# Single node
		if cur.getNext() == self.head:
			if cur.getVal() == val:
				self.head = None
				del cur
				return val
			else:
				return None
		
		cur = cur.getNext()

		# 2 or more nodes
		while cur != self.head:
			if cur.getNext().getVal() == val:
				temp = cur.getNext()
				if temp == self.head:
					self.head = temp.getNext()
				cur.setNext(temp.getNext())
				del temp
				return val
			cur = cur.getNext()
		if cur == self.head:
			if cur.getNext().getVal() == val:
				temp = cur.getNext()
				cur.setNext(cur.getNext().getNext())
				del temp
				return val
		return None


if __name__ == '__main__':
	l = CLL()
	print 'String representation of list is:',l
	l.printList()
	print 'Length of list is:',l.getLength()

	l.addNode(10)
	print 'String representation of list is:',l
	print 'Length of list is:',l.getLength()
	l.printList()
	l.addNode(2)
	l.printList()
	l.addNode(1)
	l.addNode(4)
	l.printList()
	print 'Length of list is:',l.getLength()
	
	"""
	l.removeNode()
	l.removeNode()
	l.printList()
	l.removeNode()
	l.printList()
	l.removeNode()
	l.printList()
	"""

	n = input('Enter number to check in list: ')
	if l.contains(n):
		print 'List contains the number:',n
	else:
		print 'List DOES NOT contain the number:',n

	print 'String representation of list is:',l

	print 'Deleting the node:',l.remove(n)
	l.printList()