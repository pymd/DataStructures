class Node:
    def __init__(self):
        self.val = 0
        self.next = None

    def __str__(self):
        result = ''
        if self.val == 0 and self.next == None:
            return result
        else:
            result = str(self.val)
            return result

    def getVal(self):
        return self.val

    def getNext(self):
        return self.next

    def setVal(self, val):
        self.val = val

    def setNext(self, next):
        self.next = next
