from listNode import Node

class list:
    def __init__(self):
        self.head = None

    def createNode(self, val):
        node = Node()
        node.setVal(val)
        node.setNext(None)
        return node

    def getListLength(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.getNext()
        return length

    def addNodeAtBegin(self, val):
        """
            Time:   O(1)
        """
        node = self.createNode(val)
        node.setNext(self.head)
        self.head = node

    def addNodeAtEnd(self, val):
        """
            Time:   O(n)
        """
        node = self.createNode(val)
        current = self.getHead()
        if current is None:
            self.head = node
        else:
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(node)

    def addNodeAtPosX(self, val, pos):
        """
            Time:   O(n)
        """
        node = self.createNode(val)
        current = self.getHead()
        # Assuming node map or may not have p elements
        if current is None:
            # Insert val at head
            self.head = node
        else:
            if (pos == 0) or (pos == 1):
                # Handling the case of insertion at first position separately
                node.setNext(current)
                self.head = node
                return
            i = 1
            # Insert val at position 'p' or at end of list, which ever is smaller
            while (current.getNext() is not None) and (i < pos-1):
                current = current.getNext()
                i += 1
            node.setNext(current.getNext())
            current.setNext(node)

    def deleteFromBegin(self):
        """
            Time:   O(1)
        """
        if self.head is None:
            return
        current = self.head
        self.head = current.getNext()
        del current

    def deleteFromEnd(self):
        """
            Time:   O(n)
        """
        if self.head is None:
            return
        current = self.head
        if current.getNext() is None:
            self.head = None
            del current
        else:
            while current.getNext().getNext() is not None:
                current = current.getNext()
            ele = current.getNext()
            del ele
            current.setNext(None)

    def deleteFromPosX(self, pos):
        if self.head is None:
            return
        prev = self.head
        current = prev.getNext()

        if (pos == 0) or (pos == 1):
            self.head = prev.getNext()
            del prev
        else:
            i = 1
            while (current is not None) and i < pos-1:
                prev = current
                current = current.getNext()
                i += 1
            if current is None:
                prev.setNext(current)
            else:
                prev.setNext(current.getNext())
            del current


    def printList(self):
        """
            Time:   O(n)
        """
        current = self.head
        while current is not None:
            print current.getVal(),'->',
            current = current.getNext()
        print 'NULL'

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.head = head


if __name__ == '__main__':
    l = list()
    l.setHead(l.createNode(1))
    l.deleteFromBegin()
    l.printList()
    print 'Length of list is:',l.getListLength()
    l.addNodeAtBegin(2)
    l.addNodeAtBegin(3)
    l.printList()
    l.addNodeAtBegin(4)
    l.addNodeAtBegin(5)
    l.printList()
    l.addNodeAtEnd(10)
    l.addNodeAtEnd(15)
    l.printList()
    l.addNodeAtPosX(100,1)
    l.addNodeAtPosX(200,9)
    l.printList()

    print 'Length of list is:',l.getListLength()
    
    l.deleteFromBegin()
    l.printList()
    print 'Length of list is:',l.getListLength()
    l.deleteFromEnd()
    l.printList()
    print 'Length of list is:',l.getListLength()
    l.deleteFromPosX(6)
    l.printList()
    print 'Length of list is:',l.getListLength()