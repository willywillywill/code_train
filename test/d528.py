class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data:
            if data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
            else:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
        else:
            self.data = data
    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()




while 1:
    try:
        n = int(input())
        s = list(map(int, input().split()))
        tree = Node(s[0])
        for i in s[1:]:
            tree.insert(i)

        tree.preorder()
        print()
    except:
        break
