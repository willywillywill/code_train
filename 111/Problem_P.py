class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if self.data > data:
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
    def postorder(self):
        if self.right:
            self.right.postorder()
        if self.left:
            self.left.postorder()
        print(self.data)
        
preorder, inorder = list(map(str, "DBACEGF ABCDEFG".split()))


pre_tree = Node()
in_tree = Node()

for i in preorder:
    pre_tree.insert(i)
for i in inorder:
    in_tree.insert(i)

print(pre_tree.postorder())
print(in_tree.postorder())
