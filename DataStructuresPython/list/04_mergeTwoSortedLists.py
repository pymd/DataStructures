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

	def mergeSortedLists(self, l2):
		"""
			Merging the two sorted lists into the first list
			O(n)
		"""
		prev1 = None
		cur1 = self.head
		cur2 = l2.getHead()
		# Merge the two lists into the first list
		while (cur1 is not None) and (cur2 is not None):
			if cur1.getVal() <= cur2.getVal():
				prev1 = cur1
				cur1 = cur1.getNext()
			else:
				temp = cur2.getNext()
				if prev1 is not None:
					prev1.setNext(cur2)
				else:
					self.head = cur2
				cur2.setNext(cur1)
				prev1 = cur2
				cur2 = temp
		if cur1 is None:
			prev1.setNext(cur2)

	def _removeHead(self):
		if self.head is None:
			return
		temp = self.head
		self.head = self.head.getNext()
		temp.setNext(None)

	def recursiveSortedMerge(self, l2):
		"""
			Similar to the merge procedure of mergeSort
		"""
		if (self.getHead() is None) and (l2.getHead() is None):
			return None

		if (l2.getHead() is None) or ((self.getHead() is not None) and (self.getHead().getVal() <= l2.getHead().getVal())):
			result = self.getHead()
			self._removeHead()
			result.setNext(self.recursiveSortedMerge(l2))
			return result

		elif (self.getHead() is None) or ((l2.getHead() is not None) and self.getHead().getVal() > l2.getHead().getVal()):
			result = l2.getHead()
			l2._removeHead()
			l1 = self
			result.setNext(l2.recursiveSortedMerge(l1))
			return result

		else:
			print 'Shouldnt reach here'
			return None


if __name__ == '__main__':
	l = List()
	l.addNode(10)
	l.addNode(8)
	l.addNode(6)
	l.addNode(4)
	l.addNode(2)
	l.addNode(0)
	l.printList()

	l2 = List()
	l2.addNode(9)
	l2.addNode(7)
	l2.addNode(5)
	l2.addNode(3)
	l2.addNode(1)
	l2.printList()

	print 'Merging the two lists:'
	#l.mergeSortedLists(l2)

	# Recursively merging the two lists
	l.setHead(l.recursiveSortedMerge(l2))

	l.printList()

