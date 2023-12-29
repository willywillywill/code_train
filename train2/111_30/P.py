class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def build(preorder,inorder):
    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = node(inorder[idx])
        root.left = build(preorder, inorder[:idx])
        root.right = build(preorder, inorder[idx+1:])
        return root
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        ans.append(root.val)

preOrder,inOrder = map(list,input().split())
root = build(preOrder, inOrder)
ans = []
postOrder(root)
print(ans)