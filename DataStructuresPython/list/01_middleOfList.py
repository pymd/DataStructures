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

    def printList(self):
        current = self.head
        while current is not None:
            print current.getVal(),'->',
            current = current.getNext()
        print 'NULL'

    def addNode(self, val):
        node = self.createNode(val)
        node.setNext(self.head)
        self.head = node

    def getMiddleOfList(self):
        """
            Returns a type 'Node'
        """
        slow = self.head
        fast = self.head
        if (fast is None) or (fast.getNext() is None):
            return slow
        while True:
            if (fast is None) or (fast.getNext() is None):
                return slow
            slow = slow.getNext()
            fast = fast.getNext().getNext()

if __name__ == '__main__':
    l = List()
    l.addNode(10)
    l.addNode(6)
    l.addNode(5)
    l.addNode(4)
    l.addNode(3)
    l.addNode(2)
    l.addNode(1)
    l.printList()
    node = l.getMiddleOfList()
    if node is not None:
        print 'Middle element of list is:', node.getVal()
    else:
        print 'List is empty'
