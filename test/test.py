class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build(inorder, preorder):
    if inorder:
        idx = inorder.index(preorder.pop(-1))
        root = node(inorder[idx])
        root.left = build(inorder[:idx], preorder)
        root.right = build(inorder[idx+1:], preorder)
        return root
def preOrder(root):
    if root:
        preOrder(root.left)
        preOrder(root.right)
        print(root.val)

root = build(list("dbac"),list("abdc"))
preOrder(root)