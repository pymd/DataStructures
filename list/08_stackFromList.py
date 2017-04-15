from listNode import Node as ListNode

class Stack:
	def __init__(self):
		self.top = None

	def push(self, ele):
		temp = ListNode()
		temp.setVal(ele)
		temp.setNext(self.top)
		self.top = temp

	def pop(self):
		if self.top == None:
			return None
		else:
			temp = self.top.getVal()
			self.top = self.top.getNext()
			return temp

	def isEmpty(self):
		if self.top == None:
			return True
		return False

	def peek(self):
		return self.top

	def getTop(self):
		return self.top

	def setTop(self, top):
		self.top = top

	def __str__(self):
		result = ''
		cur = self.top
		while cur != None:
			result += str(cur) + '\n'
			cur = cur.getNext()
		return result

if __name__ == '__main__':
	s = Stack()
	s.push(10)
	s.push(20)
	print s
	s.push(30)
	s.push(40)
	print s
	print 'Element popped out is:', s.pop()
	print s
	print 'Element popped out is:', s.pop()
	print s
	print 'Element popped out is:', s.pop()
	print s
	print 'Element popped out is:', s.pop()
	print s