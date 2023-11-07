class PListNode:
    def __init__(self, coef=1, expo=0):
        self.coef = coef
        self.expo = expo
        self.next = None
class PLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0


