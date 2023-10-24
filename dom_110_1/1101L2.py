class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def insert(self, val):
        if self.val > val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = node(val)
    def postoder(self):
        if self.left:
            self.left.postoder()
        if self.right:
            self.right.postoder()
        print(self.val,end=" ")

for i in range(int(input())):
    _ = int(input())
    lst = list(map(int,input().split(",")))
    tree = node(lst[0])
    for i in lst[1:]:
        tree.insert(i)
    tree.postoder()
    print()

"""
2
8
7,4,1,5,12,8,9,15
10
9,4,1,5,12,11,10,15,2,3
"""