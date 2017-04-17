import random
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

	def addNode(self, val):
		"""
			Add node at end of list
		"""
		node = self.createNode(val)
		if self.head is None:
			self.head = node
			return node
		cur = self.head
		while cur.getNext() is not None:
			cur = cur.getNext()
		cur.setNext(node)
		return node
		

	def printList(self, length):
		cur = self.head
		ctr = 0
		while (cur is not None) and (ctr <= length):
			print cur.getVal(),'->',
			cur = cur.getNext()
			ctr += 1
		if ctr <= length:
			print 'NULL'
		else:
			print 'loop ...'

	def detectIfListHasLoop (self):
		"""
			Returns true is list has loop.
			Otherwise returns False.
		"""
		slow = self.head
		if slow is None:
			return False
		fast = self.head
		length = 0
		while (fast is not None) and ((slow != fast) or (length == 0)):
			slow = slow.getNext()
			fast = fast.getNext()
			if fast is None:
				break
			fast = fast.getNext()
			length += 1
		if (slow == fast) and (length > 0):
			return True
		else:
			return False

	def findLoopStart (self):
		"""
			Returns the start of loop in the list if there exists one.
			Otherwise returns 'None'
		"""
		slow = self.head
		if slow is None:
			return None
		fast = self.head
		length = 0
		while (fast is not None) and ((slow != fast) or (length == 0)):
			slow = slow.getNext()
			fast = fast.getNext()
			if fast is None:
				break
			fast = fast.getNext()
			length += 1
		if (slow == fast) and (length > 0):
			# has loop
			slow = self.head
			while slow != fast:
				slow = slow.getNext()
				fast = fast.getNext()
			return fast
		else:
			return None

	def findLengthOfLoopInList(self):
		"""
			Returns length of loop in list.
		"""
		slow = self.head
		if slow is None:
			return 0
		fast = self.head
		length = 0
		while (fast is not None) and ((slow != fast) or (length == 0)):
			slow = slow.getNext()
			fast = fast.getNext()
			if fast is None:
				break
			fast = fast.getNext()
			length += 1

		if (slow == fast) and (length > 0):
			slow = self.head
			while slow != fast:
				slow = slow.getNext()
				fast = fast.getNext()
			length = 0
			while (slow != fast) or (length == 0):
				fast = fast.getNext()
				length += 1
			return length
		else:
			return 0

def createLoopedLinkedList (n,y,totalNodesInList):
	l = List()
	vals = range(totalNodesInList)
	random.shuffle(vals)
	for ctr, val in enumerate(vals):
		if ctr == n-1:
			loopStart = l.addNode(val)
			print '(Loop starts at:' + str(loopStart.getVal()) + ')'
		elif ctr == totalNodesInList-1:
			lastNode = l.addNode(val)
			lastNode.setNext(loopStart)
		else:
			l.addNode(val)
	return l

if __name__ == '__main__':
	n = input('Enter the value of n:')
	y = input('Enter the value of loop length:')
	totalNodesInList = n + y - 1

	l = createLoopedLinkedList(n,y,totalNodesInList)
	l.printList(totalNodesInList)

	print ''
	hasLoop = l.detectIfListHasLoop()
	print 'Does the linked list has a loop:',hasLoop
	if hasLoop:
		start = l.findLoopStart()
		print 'The loop starts at:',start.getVal()
		print 'The length of loop is:',l.findLengthOfLoopInList()
