class node:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None
    def insert(self, val):
        if self.val:
            if self.val > val:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = node(val)
            else:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = node(val)
        else:
            self.val = val



n = int(input())
for _ in range(int(input())):
    pass